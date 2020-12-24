
from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
from app.models import User
from django.contrib.auth import authenticate
from app.utils import getShoeWithMax, serialize, parseOne, parseMany
from django.contrib.auth import logout as AuthLogout


def current_datetime(request):

    return render(request, 'app/tables.html')
def dashboard(request):
    session = request.session
    context = {
        "menu_active": 1
    }
    if session.get('user', False):
        user = session.get('user', None)
        context['user'] = parseOne(user)

    return render(request, 'app/dashboard.html', context)

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
    
# Create your views here.
