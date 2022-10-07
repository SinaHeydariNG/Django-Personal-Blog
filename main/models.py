from tabnanny import verbose
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class SiteInfo(models.Model):
    title = models.CharField(max_length=225)
    description = RichTextField()
    location = models.CharField(max_length=225 , default=1)
    phone = models.CharField(max_length=225 , default=1)
    logo = models.ImageField(upload_to = 'logo/%y/%m/%d/')
    email = models.EmailField(default='imsinacoder@gamil.com')
    copyright = models.CharField(max_length=225)

    class Meta:
        verbose_name = "Information"
        verbose_name_plural = "Informations" 

    def __str__(self):
        return "YOUR SITE INFO . DONT ADD ANOTHER ONE !!!"




   
class Skills(models.Model):
    title = models.CharField(max_length=225)
    precentage = models.IntegerField()
    description = RichTextField()
    iamge = models.ImageField(upload_to = 'skills/%y/%m/%d/' , blank = True , default = 'img.jpg')


    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills" 

    def __str__(self):
        return self.title




class Services(models.Model):
    title = models.CharField(max_length=225)
    subtitle = models.CharField(max_length=225)
    description = RichTextField()
    image = models.ImageField(upload_to = 'services/%y/%m/%d/' , blank = True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services" 

    def __str__(self):
        return self.title        


