
from dataclasses import fields
from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from blog.models import Post
from .models import Profile

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)   
    password = forms.CharField(widget=forms.PasswordInput)  


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content',]    



class UserUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']      


class UpdateImageProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image',]        