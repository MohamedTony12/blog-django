
from django import forms
from .models import Comment


class FormCommnet(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'email', 'comment_text']


