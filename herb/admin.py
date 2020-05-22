from django.contrib import admin
from .models import Herbstype,Herbs,Prestype,Pres,Achs,home_line,herb_sel,pres_sel,achs_sel,file_open

# Register your models here.
@admin.register(Herbstype)
class HerbstypeAdmin(admin.ModelAdmin):
    list_display = ('id','type_name')

@admin.register(Herbs)
class HerbsAdmin(admin.ModelAdmin):
    list_display = ('title','Herbs_type','image','created_time','last_updated_time')

@admin.register(Prestype)
class PrestypeAdmin(admin.ModelAdmin):
    list_display = ('id','type_name')

@admin.register(Pres)
class PresAdmin(admin.ModelAdmin):
    list_display = ('title','created_time','image','last_updated_time')

@admin.register(Achs)
class AchsAdmin(admin.ModelAdmin):
    list_display = ('title','created_time','image','last_updated_time')

@admin.register(home_line)
class home_lineAdmin(admin.ModelAdmin):
    list_display = ('herb_title','pres_title','achs_title')

@admin.register(herb_sel)
class herb_selAdmin(admin.ModelAdmin):
    list_display = ('id','herb_title')

@admin.register(pres_sel)
class pres_selAdmin(admin.ModelAdmin):
    list_display = ('id','pres_title')

@admin.register(achs_sel)
class achs_selAdmin(admin.ModelAdmin):
    list_display = ('id','achs_title')

@admin.register(file_open)
class file_openAdmin(admin.ModelAdmin):
    list_display = ('title','files')