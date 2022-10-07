from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404
from main.models import SiteInfo
from .models import Project
# Create your views here.

def detail(request , slug):
    information = SiteInfo.objects.last()  
    project = get_object_or_404(Project , slug = slug)
    context = {
        "information" : information,
        "project" : project,
}
    return render(request , 'projects/detail.html' , context)