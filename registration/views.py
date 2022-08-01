from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def signin_view(request):
    next = request.POST.get('next','/')
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    messages.info(request,'Logged in successfully')
                    messages.info(request,f'Welcome {username}')
                else:
                    messages.error(request,'Username or Password is wrong!')
            else:
                messages.error(request,'Something went wrong')
                messages.error(request,form.errors)
            
    return redirect(next)
    
def signout_view(request):
    return

def signup_view(request):
    return

def reset_view(request):
    return