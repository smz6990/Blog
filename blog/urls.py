from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('',index_view,name='index'),
    path('<int:pid>/',blog_single_view,name='single'),
    path('category/<str:cat_name>/',index_view,name='category'),
    path('tag/<str:tag_name>/',index_view,name='tag'),
    path('search/',search_view,name='search')
    
    
]