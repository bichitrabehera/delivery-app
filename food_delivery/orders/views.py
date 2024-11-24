# orders/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # Home page view

def about(request):
    return render(request, 'about.html')  # About page view

def admin_login(request):
   return render(request, 'admin/login.html')   # Admin login view

def user_login(request):
    return render(request, 'user/login.html')  # User login view

def forgot_password(request):
  
    return render(request, 'user/forgot_password.html')
def user_login(request):
    # Logic for user login
    return render(request, 'user/login.html')

def forgot_password(request):
    # Logic for forgot password
    return render(request, 'user/forgot_password.html')
def register(request):
    # Logic for user registration
    return render(request, 'user/register.html')