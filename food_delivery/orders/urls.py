# orders/urls.py

from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path('', views.home, name='home'),

      path('about/', views.about, name='about'),
    path('admin_login/', views.admin_login, name='admin_login'),  # Define admin_login URL
    path('user_login/', views.user_login, name='user_login'),
     path('forgot-password/', views.forgot_password, name='forget_password'),
     path('user-login/', views.user_login, name='user_login'),
    path('forgot-password/', views.forgot_password, name='forget_password'),  # The new URL pattern
   path('register/', views.register, name='register'),
]
