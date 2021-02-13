import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def about(request):
    return render(request,'generator/about.html')


def password(request):
    password=''
    chars=list('abcdefghijklmnopqrstuvwxyz')
    print(chars)
    print(list('abcdefghijklmnopqrstuvwxyz'.upper()))
    length=int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        chars.extend(list('abcdefghijklmnopqrstuvwxyz'.upper()))

    if request.GET.get('special'):
        chars.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        chars.extend(list('0123456789'))

    for i in range(length):
        password+=random.choice(chars)
    return render(request,'generator/password.html',{'password':password})