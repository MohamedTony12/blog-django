
from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Comment
from .forms import FormCommnet,CreateNewPostForm
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
from django.contrib.auth.decorators import login_required


def blog_home(request):
    if 'q' in request.GET:
        q = request.GET['q']
        post = Post.objects.filter(title__icontains=q)
    else:
        post = Post.objects.all().order_by('-create_at')
        
    paginator = Paginator(post,2)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)        
    context = {
        'posts': post,
    }
    return render(request, 'blog/index.html', context)


def post_detail(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    comment = Comment.objects.filter(post=post)
    if request.method == 'POST':
        form = FormCommnet(data=request.POST)
        if form.is_valid():
            n = form.save(commit=False)
            n.comment_text = form.cleaned_data.get('comment_text')
            n.post = post
            n.save()
            return redirect('/')
    else:
        form = FormCommnet(data=request.POST)
    context ={
        'post_detail':post,
        'comments':comment,
        'form':form
    }
    return render(request, 'blog/post_details.html', context)

def comment_read_all(request,comment_id,post_id):
    post = get_object_or_404(Post,id=post_id)
    comment = Comment.objects.get(id=comment_id)
    

    context ={
        'comments':comment,
        'post':post,
        
    }
    return render(request, 'blog/readcomment.html', context)



@login_required(login_url='user:user_login')
def create_new_post(request):
    if request.method == 'POST':
        form = CreateNewPostForm(request.POST)
        if form.is_valid():
            n = form.save(commit=False)
            n.author = request.user
            n.title = form.cleaned_data.get('title')  
            n.content = form.cleaned_data.get('content') 
            n.save()
            messages.success(request,'Post Created Successfully') 
            return redirect('/')
    else:
        form = CreateNewPostForm(request.POST) 

    return render(request, 'blog/createpost.html', {'form':form})    



    
       