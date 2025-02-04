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


class packageAdmin(admin.ModelAdmin):
    list_display=['city','package_image','package_name','discount_price','full_price','Availability','no_of_days']

admin.site.register(packages,packageAdmin)

class citypageAdmin(admin.ModelAdmin):
    list_display=['city_name','city_image','city_description','city_gallery1','city_gallery2','city_gallery3','city_gallery4','city_gallery5','city_map']
    
admin.site.register(Basecitypage,citypageAdmin)

