from multiprocessing import context
from .models import Post,Comment

def last_post(request):
    post = Post.objects.all().order_by('-create_at')[:5]
    comment = Comment.objects.filter(active=True).order_by('-comment_at')[:5]
    context = {
        'lastpost':post,
        'lastcomment':comment
    }
    return context

