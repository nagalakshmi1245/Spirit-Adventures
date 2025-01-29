from django.contrib import admin
from .models import category,sub_category
# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    list_display=['name']
class sub_categoryAdmin(admin.ModelAdmin):
    list_display=['name']

admin.site.register(category,categoryAdmin)
admin.site.register(sub_category,sub_categoryAdmin)
