from django.contrib import admin
from . import models
from django.utils.html import format_html
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    def thumbnail(self , object):
        return format_html(" <img src='{}' style='width: 40px;'>".format(object.image.url))
    list_display = ['title' , 'subtitle' , 'thumbnail' , 'author' , 'category' , 'date']
    list_editable = ['subtitle']
    search_fields = ['title' , 'subtitle'  , 'author' , 'date']
    list_filter = [ 'author' , 'date' , 'category' ]



admin.site.register(models.Blog , BlogAdmin)
admin.site.register(models.Category)
admin.site.register(models.Likes)
admin.site.register(models.Comments)