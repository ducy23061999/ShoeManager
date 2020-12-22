from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    context = {
        "menu_active": 0
    }
    return render(request, 'app/index.html', context)

def category(request):
    context = {
        "menu_active": 1
    }
    return render(request, 'app/category.html', context)

def cart(request):
    return render(request, 'app/cart.html')

def login(request):
    context = {
        "menu_active": 3
    }
    return render(request, 'app/login.html', context)

def register(request):
    context = {
        "menu_active": 3
    }
    return render(request, 'app/register.html', context)

def detail(request):
    context = {
        "menu_active": 1
    }
    return render(request, 'app/single-product.html', context)

