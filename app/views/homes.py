from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from app.models import Shoe, Size, Stock
from app.utils import getShoeWithMax, serialize, parseOne, parseMany


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
    session = request.session

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
        "deal_of_week": dealOfWeek,

    }
    if session.get('user', False):
        user = session.get('user', None)
        context['user'] = parseOne(user)

    return render(request, 'app/category.html', context)

def cart(request):
    session = request.session
    context = {
        "menu_active": 1
    }
    if session.get('user', False):
        user = session.get('user', None)
        context['user'] = parseOne(user)

    return render(request, 'app/cart.html', context)

def login(request):
   session = request.session
   if request.method == 'GET':

       if session.get('user', False):
            return redirect('/')
       else:
            context = {
                "menu_active": 3
            }
            return render(request, 'app/login.html', context)
   else:
       username = request.POST.get('username', '')
       password = request.POST.get('password', '')
       context = {
           "menu_active": 3
       }
       user = authenticate(username=username, password=password)

       if user:
           session['user'] = serialize(user)
           return redirect('/cart/')
       else:
           return redirect('/login/')

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

