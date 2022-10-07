from django import forms
from . import models
class CommentBlogForm(forms.ModelForm):
    class Meta:
        model = models.Comments
        fields = ['content' , 'parent']