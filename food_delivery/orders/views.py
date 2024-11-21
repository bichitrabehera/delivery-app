# orders/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # 'index.html' will be in the 'frontend' folder based on DIRS
