from django.contrib import admin
from blog.models import Category,Post,Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title','id','author','status','counted_views','published_date','created_date')
    list_filter = ('status','author')
    search_fields = ('title','content')
    
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name','post','email','approved','created_date')
    list_filter = ('post','approved')
    search_fields = ('post','name','email')

admin.site.register(Category)
    