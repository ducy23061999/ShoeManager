from django.shortcuts import render
from django.http import HttpResponse
import datetime

def current_datetime(request):

    return render(request, 'app/tables.html')

# Create your views here.
