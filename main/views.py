from django.shortcuts import render , redirect , HttpResponse
from . import models
from contact.forms import ContactForm
from blog.models import Blog , Category
from contact.models import Social , Contact
from projects.models import Project , Category as project_category
# Create your views here.


def home(request):
    projects = Project.objects.all()
    project_categories = project_category.objects.all()
    contacts = Contact.objects.all()
    socials = Social.objects.all()
    blogs = Blog.objects.all().order_by('-date')
    categories = Category.objects.all().order_by('-title') 
    contact = ContactForm()
    information = models.SiteInfo.objects.last()  
    skills = models.Skills.objects.all()
    services = models.Services.objects.all()
    title = "Home"
    context = {
        "projects" : projects,
        "project_categories" : project_categories,
        "contacts" : contacts,
        "socials" : socials,
        "categories" : categories,
        "blogs" : blogs,
        "contact" : contact,
        "services" : services,
        'skills' : skills,
        'information' : information,
        "title" : title}
    return render(request , 'main/main.html' , context)

