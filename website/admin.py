from django.contrib import admin
from website.models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','email','created_date')
    empty_value_display = '-empty-'
    list_filter = ('email','name')
    search_fields = ('email','subject','message')