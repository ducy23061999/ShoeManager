from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):

    return render(request, 'app/index.html')

def category(request):
    return render(request, 'app/category.html')

def cart(request):
    return render(request, 'app/cart.html')

def login(request):
    return render(request, 'app/login.html')

def register(request):
    return render(request, 'app/register.html')

def detail(request):
    return render(request, 'app/single-product.html')

