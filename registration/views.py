from django.shortcuts import redirect, render
from django.urls import reverse
from registration.forms import UserAuthenticationForm , CustomUserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes


# Create your views here.
def signin_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserAuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    messages.info(request,'Logged in successfully')
                    messages.info(request,f'Welcome , {username}')
                else:
                    messages.error(request,'Username or Password is wrong!')
            else:
                messages.error(request,'Something went wrong')
                messages.error(request,form.errors)
            
            next = request.POST.get('next','/')
            return redirect(next)
        
        else: #request.method == 'GET'
            form = UserAuthenticationForm()
            next = request.GET.get('next','/')
            context = {'form':form,'next':next}
            
            return render(request,'registration/signin.html',context)
    
    next = request.GET.get('next','/')
    return redirect(next)


@login_required(redirect_field_name='next',login_url='/registration/signin/',)
def signout_view(request):
    next = request.GET.get('next','/')
    logout(request)
    return redirect(next)

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                username = request.POST['username']
                email = request.POST['email']
                try:
                    username = User.objects.get(username=username)
                except:
                    pass
                else:
                    messages.error(request,'Username is taken')
                    form = CustomUserCreationForm()
                    next = request.POST.get('next','/')
                    return  render(request,'registration/signup.html',{'form':form,'next':next})
                try:
                    email = User.objects.get(email=email)
                except:
                    user = form.save()
                    login(request,user)
                    messages.success(request,'Account created successfully')
                    messages.success(request,f'Welcome , {user.username}')
                    next = request.GET.get('next','/')
                    return redirect(next)
                else:               
                    messages.error(request,'Email is taken')
            else:
                messages.error(request,'Something went wrong')
                messages.error(request,form.errors)
                
            next = request.POST.get('next','/')
        else:
            next = request.GET.get('next','/')
        form = CustomUserCreationForm()
        return  render(request,'registration/signup.html',{'form':form,'next':next})
    
    next = request.GET.get('next','/')
    return redirect(next)

def password_reset_request_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            password_reset_form = PasswordResetForm(request.POST)
            if password_reset_form.is_valid():
                data = password_reset_form.cleaned_data['email']
                associated_users = User.objects.filter(Q(email=data))
                if associated_users.exists():
                    for user in associated_users:
                        subject = "Password Reset Requested"
                        email_template_name = "registration/password_reset_email.txt"
                        c = {
                        "email":user.email,
                        'domain':'127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                        }
                        email = render_to_string(email_template_name, c)
                        try:
                            send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
                        except BadHeaderError:
                            return HttpResponse('Invalid header found.')
                        messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
                        return redirect (reverse('registration:password_reset_done'))
                messages.error(request, 'An invalid email has been entered.')
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="registration/password_reset.html", context={"password_reset_form":password_reset_form})