from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('',blog_index_view,name='index'),
    path('<int:pid>/',blog_single_view,name='single'),
    
]