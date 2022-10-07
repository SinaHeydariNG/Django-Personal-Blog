from dataclasses import fields
from django.forms import ModelForm
from django import forms
from .models import Contact
# define the class of a form
class ContactForm(ModelForm):
    class Meta:
        model = Contact	
        fields = ['name' , 'email' , 'subject' , 'message']
        widgets = {
        'email': forms.EmailInput(attrs={'placeholder': 'email'}),
        'name': forms.TextInput(attrs={'placeholder': 'name'}),
        'message': forms.Textarea(attrs={'placeholder': 'message'}),
    }
    def clean(self):
        super(ContactForm, self).clean()
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        message = self.cleaned_data.get('message')
        BAD_WORDS = ['fuck']
        if len(email) < 5:
            self._errors['email'] = self.error_class([
                'Minimum 5 characters required!'])   
        if len(message) < 10 or any([word in message.lower() for word in BAD_WORDS]):
            self._errors['message'] = self.error_class([
                "Minimum 10 characters required!"
            ])          
        return self.cleaned_data

