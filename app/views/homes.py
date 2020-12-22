from django.shortcuts import render
from django.http import HttpResponse
from setuptools.command.develop import develop

from app.models import Shoe, Size, Stock
from app.utils import getShoeWithMax
import datetime

def index(request):
    shoes = Shoe.objects.all()
    dealOfWeek = getShoeWithMax(shoes)

    context = {
        "menu_active": 0,
        "deal_of_week": dealOfWeek
    }

    return render(request, 'app/index.html', context)

def category(request):

    sizes = Size.objects.all()

    selectedSize = request.GET.get('size_id', '')
    shoes = []
    dealOfWeek = getShoeWithMax(Shoe.objects.all())

    if selectedSize:
        def shoe(x):
            return x.shoe

        stocks = Stock.objects.filter(size=selectedSize)
        shoes = map(shoe, stocks)
    else:
        shoes = Shoe.objects.all()


    context = {
        "menu_active": 0,
        "sizes": sizes,
        "shoes": shoes,
        "deal_of_week": dealOfWeek
    }

    return render(request, 'app/category.html', context)

def cart(request):
    return render(request, 'app/cart.html')

def login(request):
   if request.method == 'GET':
        context = {
            "menu_active": 3
        }
        return render(request, 'app/login.html', context)
   else:
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

