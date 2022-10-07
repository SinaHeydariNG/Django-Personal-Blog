from django.shortcuts import render
from . import serilizer
from blog.models import Blog
from projects.models import Project
from rest_framework import generics , permissions
# Create your views here.


# Blog APIviews

class BlogListView(generics.ListCreateAPIView):
    serializer_class = serilizer.BlogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Blog.objects.filter(author = user)
    def perform_create(self, serializer):
        serializer.save(author = self.request.user)    

class BlogDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serilizer.BlogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Blog.objects.filter(author = user)
    def perform_create(self, serializer):
        serializer.save(author = self.request.user)    

class BLogImportantList(generics.ListAPIView):
    serializer_class = serilizer.BlogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Blog.objects.filter(author = user , important = True)

class BlogToImportant(generics.UpdateAPIView):
    serializer_class = serilizer.BlogImportantSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Blog.objects.filter(author = user )

    def perform_update(self,  serializer):
        serializer.instance.important = True
        serializer.save()    


# Project APIviews

class ProjectListView(generics.ListCreateAPIView):
    serializer_class = serilizer.ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.all()

    def perform_create(self, serializer):
        serilizer.save()    

class ProjectUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serilizer.ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.all()

    def perform_create(self, serializer):
        serilizer.save()