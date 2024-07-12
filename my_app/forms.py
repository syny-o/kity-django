from django import forms
from django.forms import ModelForm

from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'message': 'Your Message'
        }
        help_texts = {
            'name': 'Enter your name',
            'email': 'Enter your email',
            'message': 'Enter your message'
        }
        error_messages = {
            'name': {
                'required': 'Please enter your name'
            },
            'email': {
                'required': 'Please enter your email'
            },
            'message': {
                'required': 'Please enter your message'
            }
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'})
        }