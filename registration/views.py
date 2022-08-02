from django.shortcuts import redirect, render
from registration.forms import UserAuthenticationForm , CustomUserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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

def reset_view(request):
    return