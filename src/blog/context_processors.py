from multiprocessing import context
from .models import Post

def last_post(request):
    post = Post.objects.all().order_by('-create_at')[:5]
    context = {
        'lastpost':post
    }
    return context