
from django import forms
from .models import Comment,Post


class FormCommnet(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'email', 'comment_text']


class CreateNewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']