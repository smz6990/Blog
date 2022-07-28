from django.urls import path
from website.views import website_index

app_name = 'website'

urlpatterns = [
    path('',website_index,name='index'),
    
]