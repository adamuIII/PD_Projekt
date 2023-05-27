from django.shortcuts import render
from .models import Game

def index(request):
    return render(request, "gameshop/index.html")

def products(request):
    products = Game.objects.all()
    return render(request, 'gameshop/products.html', {'products': products})

def regulamin(request):
    return render(request, 'gameshop/regulamin.html')

def pomoc(request):
    return render(request, 'gameshop/pomoc.html')

def login(request):
    return render(request, 'gameshop/authenticate/login.html')

def register(request):
    return render(request, 'gameshop/authenticate/register.html')


