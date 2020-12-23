from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from app.models import Shoe, Size, Stock, User
from app.utils import getShoeWithMax, serialize, parseOne, parseMany
from django.contrib.auth import logout as AuthLogout

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
           context['error'] = "Login Failed"
           return render(request, 'app/login.html', context)

def logout(request):
    try:
        AuthLogout(request)
        del request.session['user']
    except KeyError:
        pass
    return redirect('/')



def register(request):
    session = request.session
    context = {
        "menu_active": 4
    }

    if request.method == 'GET':
        if session.get('user', False):
            return redirect('/')
        else:
            context = {
                "menu_active": 4
            }
            return render(request, 'app/user_register.html', context)
    else:
        try:
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            repassword = request.POST.get('repassword', '')
            firstname = request.POST.get('firstname', '')
            lastname = request.POST.get('lastname', '')

            if password == repassword:
                if User.objects.filter(username=username).filter():
                    context['error'] = "Username already taken"
                    return render(request, 'app/user_register.html', context)
                else:
                    User.objects.create_user(username, password, firstname, lastname)

                    return redirect("/login")
            else:
                context['error'] = "Password not match"
                return render(request, 'app/user_register.html', context)
        except User.DoesNotExist:
            return redirect("/")

def detail(request):
    context = {
        "menu_active": 1
    }
    return render(request, 'app/single-product.html', context)

