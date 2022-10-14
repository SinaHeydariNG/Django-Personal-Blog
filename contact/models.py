from tabnanny import verbose
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.




class Subject(models.TextChoices):
    PROJECT = "PROJECT" , "PROJECT"
    HIRE = "HIRE" , "HIRE"
    MESSAGE = "MESSAGE" , "MESSAGE"


BAD_WORDS = ['fuck' , 'asss' , 'shit']

def bad_words_validators(message):
    if any([word in message.lower() for word in BAD_WORDS]):
        raise ValidationError("Your content cotains bad words! , consider changing them")

class Contact(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    subject = models.CharField(max_length=20 , choices=Subject.choices , default=Subject.PROJECT)
    message = models.TextField(validators=[bad_words_validators])
    activate = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.subject   



class Social(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'social/%y/%m/%d/')
    url = models.URLField(max_length=200 , unique=True)


    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Socials"
    
    def __str__(self):
        return self.title
