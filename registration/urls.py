from django.urls import path
from registration.views import *
from django.contrib.auth import views as auth_views

app_name = 'registration'

urlpatterns = [
    path('signin',signin_view,name='signin'),
    path('signout',signout_view,name='signout'),
    path('signup',signup_view,name='signup'),
    
    path("password_reset", 
        password_reset_request_view, 
        name="password_reset"), 
    
    path('password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
        name='password_reset_done'),
     
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html",
        post_reset_login=False,success_url='/registration/reset/done/'),
    name='password_reset_confirm'),
    
    path('reset/done/',
        auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'),      
    
]
