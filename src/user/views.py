from pydoc import pager
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm,UpdatePostForm,UpdateImageProfile,UserUpdate
from blog.models import Post
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator


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
            return redirect('user:user_login')
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
                return redirect('user:user_profile')   
            else:
                messages.error(request,'please check your field and try again') 
    else:
        form = LoginForm()       
    return render(request,'user/login.html',{'form':form})

@login_required(login_url='user:user_login')
def user_logout(request):
    user = request.user
    if user.is_authenticated:
        logout(request)
        messages.success(request,'thanks')
    return redirect('/')   

@login_required(login_url='user:user_login')
def user_profile(request):
    post = Post.objects.filter(author=request.user).order_by('-create_at')
    post_count = Post.objects.filter(author=request.user)
    paginator = Paginator(post,2)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.pag(paginator.num_pages)        
    context = {
        'posts':post,
        'page':page,
        'post_count':post_count
    }
    return render(request,'user/profile.html',context)    

@login_required(login_url='user:user_login')
def user_update_post(request,post_id):
    post = Post.objects.filter(author=request.user)
    post_update = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = UpdatePostForm(request.POST,instance=post_update)
        if form.is_valid():
            n = form.save(commit=False)
            n.title = form.cleaned_data.get('title')
            n.content = form.cleaned_data.get('content')
            n.save()
            messages.success(request,'Updated successfully')
            return redirect('user:user_profile')
    else:
        form = UpdatePostForm(instance=post_update) 
    context = {
        'posts':post,
        'form':form,
        'post_update':post_update

    }
    return render(request,'user/updatepost.html',context)    


def edit_profile_user(request):
    if request.method == 'POST':
        form_user_edit = UserUpdate(request.POST,instance=request.user)
        form_user_image = UpdateImageProfile(request.POST,request.FILES,instance=request.user.profile)
        if form_user_edit.is_valid() and form_user_image.is_valid():
            n_u = form_user_edit.save(commit=False)
            n_p = form_user_image.save(commit=False)
            n_u.username = form_user_edit.cleaned_data.get('username')
            n_u.email = form_user_edit.cleaned_data.get('email')
            n_p.image = form_user_image.cleaned_data['image']
            n_u.save()
            n_p.save()
            messages.success(request,'Edited was Successfully')
            return redirect('user:user_profile')
    else:
        form_user_edit = UserUpdate(instance=request.user)
        form_user_image = UpdateImageProfile(request.POST,request.FILES,instance=request.user.profile)

    context = {
            'user_form':form_user_edit,
            'profile_form':form_user_image,
            
            
        }
    return render(request,'user/updateuserprofile.html',context)    

def post_delete(request,post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    messages.success(request,'deleted was Successfully')
    return redirect('user:user_profile')
    
