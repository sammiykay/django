from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class ImageForm(ModelForm):
    class Meta:
        model = Name
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'title'})
        }

class Customername(ModelForm):
    class Meta:
        model = Information
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'title'}),
            'message': forms.Textarea(attrs={'class': 'message'})
        }