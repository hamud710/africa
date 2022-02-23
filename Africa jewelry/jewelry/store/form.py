from dataclasses import field, fields
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm

from .models import User
from django import forms

class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter username' } ) )
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Email' } ) )
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password' } ) )
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password' } ) )
    class Meta:
        model = User
        fields = ['username','email','password1','password2']