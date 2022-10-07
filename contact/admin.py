from django.contrib import admin
from . import models
from django.utils.html import format_html
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name' , 'email' , 'subject' , 'activate']
    search_fields = ['name' , 'email' , 'subject']
    list_filter = [ 'subject' , 'activate' ]

class SocialAdmin(admin.ModelAdmin):
    def thumbnail(self , object):
        return format_html(" <img src='{}' style='width: 40px;'>".format(object.image.url))
    list_display = ['title' , 'thumbnail']
    search_fields = ['title']



admin.site.register(models.Contact , ContactAdmin)
admin.site.register(models.Social , SocialAdmin)