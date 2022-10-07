from django.shortcuts import render , redirect , HttpResponse
from . import models
from .forms import ContactForm
from main.models import SiteInfo
from django.contrib import messages
# Create your views here.

def message(request):
    information = SiteInfo.objects.last()  
    if request.method == "POST":
        form = ContactForm(request.POST)
        print(request.POST['name'])
        if form.is_valid():
            print("YEAH")
            new_contact = models.Contact.objects.create(
                name = form.cleaned_data['name'],
                email = form.cleaned_data['email'],
                message = form.cleaned_data['message'],
                subject = form.cleaned_data['subject']
            )
            new_contact.save()
            return redirect("main:home")  
        else:
            information = SiteInfo.objects.last()
            messages.error(request , form.errors)
            context=  {
                "information" : information,
                "form" : form}
            return render(request, "contact/add.html", context)
    else:
        form = ContactForm    
    
    context = {
        "information" : information,
        "form" : form
        }        
    return render(request , 'contact/add.html' , context)
         
