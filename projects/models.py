from email.policy import default
from django.db import models
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.db.models.signals import pre_save
# Create your models here.


class Level(models.TextChoices):
    ELEMENTARY = "ELEMENTARY" , "ELEMENTARY"
    INTERMEDIATE = "INTERMEDIATE" , "INTERMEDIATE"
    ADVANCED = "ADVANCED" , "ADVANCED"

class Project(models.Model):
    title = models.CharField(max_length=225)
    subtitle = models.CharField(max_length=225)
    duration  = models.IntegerField()
    level = models.CharField(max_length=20 , choices=Level.choices , default=Level.INTERMEDIATE)
    slug = models.SlugField(blank=True , null=True)
    tags = TaggableManager()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('category' , on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'project/%y/%m/%d/' ,default = 'default.png')

    gallery_1 = models.ImageField(upload_to = 'project/%y/%m/%d/' , blank = True , default = 'default.png')
    gallery_2 = models.ImageField(upload_to = 'project/%y/%m/%d/' , blank = True ,default = 'default.png')
    gallery_3 = models.ImageField(upload_to = 'project/%y/%m/%d/' , blank = True ,default = 'default.png')
    gallery_4 = models.ImageField(upload_to = 'project/%y/%m/%d/' , blank = True ,default = 'default.png')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title    


def slugify_pre_save(sender , instance , *args , **kwargs):

    title = instance.title
    slug = instance.slug

    if slug is None:
        instance.slug = slugify(title)

pre_save.connect(slugify_pre_save , Project)


class Category(models.Model):
    title = models.CharField(max_length=225)