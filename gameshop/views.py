from django.shortcuts import render

def index(request):
    return render(request, "gameshop/index.html")

def products(request):
    return render(request, 'gameshop/products.html')

def regulamin(request):
    return render(request, 'gameshop/regulamin.html')

def pomoc(request):
    return render(request, 'gameshop/pomoc.html')

def login(request):
    return render(request, 'gameshop/login.html')

def register(request):
    return render(request, 'gameshop/register.html')


