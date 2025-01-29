from django.contrib import admin
from .models import *
# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    list_display=['name']
class sub_categoryAdmin(admin.ModelAdmin):
    list_display=['name']

admin.site.register(category,categoryAdmin)
admin.site.register(sub_category,sub_categoryAdmin)

class contactAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email','phone','address']
admin.site.register(contact,contactAdmin)