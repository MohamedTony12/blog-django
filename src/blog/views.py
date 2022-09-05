
from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Comment
from .forms import FormCommnet


def blog_home(request):
    post = Post.objects.all()
    context = {
        'posts': post
    }
    return render(request, 'blog/index.html', context)


def post_detail(request,post_id):
    user = request.user
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



