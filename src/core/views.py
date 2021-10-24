
from django.shortcuts import render


def homepage(request):
    return render(request, 'homepage.html')


def load_more(request):
    return render(request, 'load_more.html')
