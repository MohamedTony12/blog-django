
from django.urls import path
from .import views

app_name = 'user'

urlpatterns = [
    path('register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('profile/', views.user_profile, name='user_profile'),
    path('user_update_post/<str:post_id>/', views.user_update_post, name='user_update_post'),
]
