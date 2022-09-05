
from django import forms
from .models import Comment


# class CreateUserComment(UserCreationForm):
#     username = forms.CharField(
#         label='username', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     email = forms.EmailField(label='email', widget=forms.EmailInput(
#         attrs={'class': 'form-control'}))
#     password1 = forms.EmailField(
#         label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     password2 = forms.EmailField(label='repeat password', widget=forms.PasswordInput(
#         attrs={'class': 'form-control'}))

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


class FormCommnet(forms.ModelForm):
    # username = forms.CharField(
    #     label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # email = forms.EmailField(label='Email', widget=forms.EmailInput(
    #     attrs={'class': 'form-control'}))
    # comment_text = forms.CharField(
    #     label='Comment text', widget=forms.Textarea(attrs={'class': 'form-control','cols':30}))   

    class Meta:
        model = Comment
        fields = ['username', 'email', 'comment_text']


