
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField()
    create_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    username = models.CharField( max_length=150)
    email = models.EmailField(max_length=254)
    comment_text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_at = models.DateTimeField( auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.username
    