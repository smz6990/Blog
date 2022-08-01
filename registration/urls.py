from django.urls import path
from registration.views import *

app_name = 'registration'

urlpatterns = [
    path('signin',signin_view,name='signin'),
    path('signout',signout_view,name='signout'),
    path('signup',signup_view,name='signup'),
    path('reset-password',reset_view,name='reset_password'),
    
    
]
