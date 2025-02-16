from django.contrib import admin
from contact import models
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id','first_name','last_name','phone',
    ordering = '-id',
    list_filter = 'created_date',
    search_fields = 'first_name','last_name',
    
