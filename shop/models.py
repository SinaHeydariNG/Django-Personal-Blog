from email.policy import default
from itertools import product
from statistics import quantiles
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.


class Products(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    subtitle = models.CharField(max_length=225 , blank=True , null=True)
    price = models.DecimalField(max_digits=6 , decimal_places=2)
    discount_price = models.IntegerField(blank = True , null = True)
    image = models.ImageField(upload_to = 'products/%y/%m/%d' , default = 'test.img')
    decription = RichTextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True , null=True)
    category = models.ForeignKey('Category' , on_delete=models.CASCADE , null=True , blank=True)

    def save(self , *args , **kwargs):
        self.slug = slugify(self.title)
        super(Products , self).save(*args , **kwargs)

    def get_absolute_url(self):
        return self.slug    


    class Meta:
        ordering = ['-date_updated']

    def __str__(self):
        return "{} from {}".format(self.title , self.user)


class Category(MPTTModel):
    title = models.CharField(max_length=225)    
    slug = models.SlugField(unique=True , null=True , blank=True)
    parent = TreeForeignKey('self' , blank=True , null=True , related_name='children' , on_delete=models.CASCADE)

    def save(self , *args , **kwargs):
        self.slug = slugify(self.title)
        super(Category , self).save(*args , **kwargs)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):                           
        full_path = [self.title]            
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent

        return ' -> '.join(full_path[::-1])
    
class OrderProduct(models.Model):
    product = models.ForeignKey(Products , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self) -> str:
        return "{} of {} from {}".format(self.quantity , self.product , self.user) 

    def get_total_price(self):
        return self.quantity * self.product.price    

class OrderList(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderProduct)
    date_ordered = models.DateTimeField()
    date_updated = models.DateTimeField(auto_now=True)
    ordered = models.BooleanField(default=False)

    def __str__(self) -> str:
        return "{} from {}".format(self.products , self.user)

    def get_final_price(self):
        total = 0.00
        for product in  self.products.all():
            total +=  int(product.get_total_price())
        return total         

class Shipping(models.TextChoices):
    PAY = "PAY" , "PAY"
    FREE = "FREE" , "FREE"


class Orders(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    products = models.ForeignKey(OrderList , on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    shipping = models.CharField(max_length=10 , choices=Shipping.choices , default=Shipping.PAY)
    address = models.CharField(max_length=225 , default=1)
    reciever = models.CharField(max_length=225 , default=1)

    def __str__(self):
        return "{} from {}".format(self.products , self.user)

    class Meta:
        verbose_name = "Submmited Orders"    
