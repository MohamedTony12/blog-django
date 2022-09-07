
from django.urls import path
from .import views

app_name = 'user'

urlpatterns = [
    path('register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('profile/', views.user_profile, name='user_profile'),
    path('update-profile/', views.edit_profile_user, name='edit_profile_user'),
    path('user_update_post/<str:post_id>/', views.user_update_post, name='user_update_post'),
    path('post-delete/<str:post_id>/', views.post_delete, name='post_delete'),
]
