from datetime import datetime
from django.db import models
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=225)
    subtitle = models.CharField(max_length=225)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    category = models.ForeignKey("Category" , on_delete=models.PROTECT)
    image = models.ImageField(upload_to = 'blog/%y/%m/%d/')
    image_1 = models.ImageField(upload_to = 'blog/%y/%m/%d/' , blank = True)
    image_2 = models.ImageField(upload_to = 'blog/%y/%m/%d/' , blank = True)
    image_3 = models.ImageField(upload_to = 'blog/%y/%m/%d/' , blank = True)
    image_4 = models.ImageField(upload_to = 'blog/%y/%m/%d/' , blank = True)
    date =  models.DateTimeField(auto_now_add=True )
    update = models.DateField(auto_now_add=True )
    content = RichTextField()   
    tags = TaggableManager(blank=True)
    slug = models.SlugField(null=True , blank=True)
    important = models.BooleanField(default=False , blank=True)

    def __str__(self):
        return self.title

class Comments(models.Model):
    blog = models.ForeignKey(Blog , on_delete=models.CASCADE , related_name='comments')
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self' , null=True , blank=True , on_delete=models.CASCADE , related_name='reply')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.user.email)  

    @property
    def children(self):
        return Comments.objects.filter(parent = self).reverse()
    @property
    def is_parent(self):
        if self.parent is None:
            return True
        else:
            return False              


class Likes(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog , on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "{} liked for {}".format(self.user , self.blog)

def slugify_pre_save(sender , instance , *args , **kwargs):

    title = instance.title
    slug = instance.slug

    if slug is None:
        instance.slug = slugify(title)

pre_save.connect(slugify_pre_save , Blog)

class Category(models.Model):
    title = models.CharField(max_length=225)

    def __str__(self):
        return self.title