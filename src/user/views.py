from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            n = form.save(commit=False)
            n.username = form.cleaned_data.get('username')
            n.email = form.cleaned_data.get('email')
            n.set_password(form.cleaned_data.get('password1'))
            n.save()
            messages.success(request,'your account have been created successfully')
            return redirect('/')
    else:
        form = RegisterForm(request.POST)       
    return render(request,'user/register.html',{'form':form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                messages.success(request,'welcome back')
                return redirect('/')   
            else:
                messages.error(request,'please check your field and try again') 
    else:
        form = LoginForm()       
    return render(request,'user/login.html',{'form':form})


def user_logout(request):
    user = request.user
    if user.is_authenticated:
        logout(request)
        messages.success(request,'thanks')
    return redirect('/')   