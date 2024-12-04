from django.urls import path
from django.contrib import admin
from . import views  # Import views from the same app

urlpatterns = [
    # Home and About pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),


    # User login, forgot password, registration, and admin login URLs
    path('user-login/', views.user_login, name='user_login'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('register/', views.register, name='register'),

]
