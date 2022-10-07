from django.contrib import admin
from . import models
from django.utils.html import format_html
# Register your models here.


class InfoAdmin(admin.ModelAdmin):
    def thumbnail(self , object):
        return format_html(" <img src='{}' style='width: 40px;'>".format(object.logo.url))
    list_display = ['title' , 'location' , 'thumbnail' , 'phone' , 'copyright']
    list_editable = [ 'location' , 'phone' , 'copyright']



class SkillsAdmin(admin.ModelAdmin):
    def thumbnail(self , object):
        return format_html(" <img src='{}' style='width: 40px;'>".format(object.iamge.url))
    list_display = ['title' , 'precentage']
    list_editable = ['precentage']
    search_fields = ['title']
    list_filter = ['precentage']

class ServicesAdmin(admin.ModelAdmin):
    def thumbnail(self , object):
        return format_html(" <img src='{}' style='width: 40px;'>".format(object.image.url))
    list_display = ['title' , 'subtitle' , 'thumbnail']
    list_editable = ['subtitle']
    search_fields = ['title' , 'subtitle']




admin.site.register(models.SiteInfo , InfoAdmin)
admin.site.register(models.Skills , SkillsAdmin)
admin.site.register(models.Services , ServicesAdmin)