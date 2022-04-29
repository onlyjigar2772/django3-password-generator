from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')    

def password(request):
    thepasswrod = ''
    chars = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIKLMNOPQRSTUVWXYZ'))
    if request.GET.get('specialchar'):
        chars.extend(list('*&^!@#$'))
    if request.GET.get('numbers'):
        chars.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))
    for _ in range(length):
        thepasswrod += random.choice(chars)

    return render(request, 'generator/password.html', {'password': thepasswrod})

def about(request):
    return render(request, 'generator/about.html')  