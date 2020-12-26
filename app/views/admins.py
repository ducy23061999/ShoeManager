
from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
from app.models import User,Shoe, Size, Stock, Cart, CartDetail
from django.contrib.auth import authenticate
from app.utils import getShoeWithMax, serialize, parseOne, parseMany
from django.contrib.auth import logout as AuthLogout


def current_datetime(request):

    return render(request, 'app/tables.html')
def dashboard(request):
    session = request.session
    cart = Cart.objects.filter(da_duyet=False).distinct()
    count = cart.count()
    
    context = {
        "menu_active": 1,
        "count": count
    }
    if session.get('user', False):
        user = session.get('user', None)
        context['user'] = parseOne(user)


        return render(request, 'app/dashboard.html', context)
    else:
        return render(request, 'app/loginadmin.html', context)

def login(request):
    session = request.session
    if request.method == 'GET':

       if session.get('user', False):
            return redirect('/')
       else:
            context = {
                "menu_active": 3
            }
            return render(request, 'app/loginadmin.html', context)
    else: 
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        context = {
            "menu_active": 3
        }
        user = authenticate(username=username, password=password)

        if user:
            session['user'] = serialize(user)
            return redirect('/dashboard/')
        else:
            context['error'] = "Login Failed"
            return render(request, 'app/loginadmin.html', context)
def logout(request):
    try:
        AuthLogout(request)
        del request.session['user']
    except KeyError:
        pass
    return redirect('/dashboard/login/')

def duyet_don_hang(request):
    session = request.session
    cart = Cart.objects.filter(da_duyet=False).distinct()
    
    context = {
        "menu_active": 1,
        "cart": cart
    }
    if session.get('user', False):
        user = session.get('user', None)
        context['user'] = parseOne(user)


        return render(request, 'app/tables.html', context)
    else:
        return render(request, 'app/loginadmin.html', context)

def duyet_don(request,don_id):
    session = request.session
    cart = Cart.objects.get(pk=don_id)
    
    context = {
        "menu_active": 1,
    }
    if cart:
        cart.da_duyet = True
        cart.save()

        return redirect('/dashboard/donhang/')
    else:
        return render(request, 'app/loginadmin.html', context)
    
    
# Create your views here.
