from django.contrib import admin
from blog.models import Category,Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('id','title','author','status','counted_views','published_date','created_date')
    list_filter = ('status','author')
    search_fields = ('title','content')
    

admin.site.register(Category)
    