from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('',website_index_view,name='index'),
    path('about/',website_about_view,name='about'),
    path('contact/',website_contact_view,name='contact'),
    
    
]