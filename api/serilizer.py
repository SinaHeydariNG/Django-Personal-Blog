from dataclasses import fields
from blog.models import Blog
from projects.models import Project
from rest_framework import serializers


# Blog Serilizers

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        date = serializers.ReadOnlyField()
        update = serializers.ReadOnlyField()
        model = Blog
        fields = ['id' , 'title' , 'subtitle' , 'date' , 'update' , 'image', 'content' , 'category' , 'important']


class BlogImportantSerializer(serializers.ModelSerializer):
    class Meta:
        date = serializers.ReadOnlyField()
        update = serializers.ReadOnlyField()
        model = Blog
        fields = ['id']
        read_only_fields = [ 'title' , 'subtitle' , 'date' , 'update' , 'image', 'content' , 'category']



# Projects Serilizers

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id' , 'title' , 'subtitle' , 'duration' ,'date' , 'category' , 'image']