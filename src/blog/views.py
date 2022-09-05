from multiprocessing import context
from django.shortcuts import render,get_object_or_404
from .models import Post


def blog_home(request):
    post = Post.objects.all()
    context = {
        'posts': post
    }
    return render(request, 'blog/index.html', context)


def post_detail(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    context ={
        'post_detail':post
    }
    return render(request, 'blog/post_details.html', context)