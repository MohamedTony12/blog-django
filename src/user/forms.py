from dataclasses import fields
from pyexpat import model
from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)   
    password = forms.CharField(widget=forms.PasswordInput)     