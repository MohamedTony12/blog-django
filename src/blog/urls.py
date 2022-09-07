
from django.urls import path
from .import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('details/<str:post_id>/', views.post_detail, name='post_detail'),
    path('comment/<str:comment_id>/<int:post_id>/', views.comment_read_all, name='read_comment'),
    path('new-post/', views.create_new_post, name='create_new_post'),
    
]
