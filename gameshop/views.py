from django.shortcuts import render, get_object_or_404, redirect
from .models import Game
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import CreateUserForm, UserLoginForm
from django.contrib import messages


def index(request):
    return render(request, "gameshop/index.html")


def products(request):
    products = Game.objects.all()
    return render(request, 'gameshop/products.html', {'products': products})


def regulamin(request):
    return render(request, 'gameshop/regulamin.html')


def pomoc(request):
    return render(request, 'gameshop/pomoc.html')


def register(request):
    form = CreateUserForm
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("gameshop:login")
    context = {'form': form}
    return render(request, 'gameshop/authenticate/register.html', context)


def game(request, slug):
    game = get_object_or_404(Game, slug=slug)
    return render(request, 'gameshop/game.html', {'game': game})

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('gameshop:index')
            else:
                form.add_error(None, 'Nieprawidłowe dane logowania.')
    else:
        form = UserLoginForm()
    return render(request, 'gameshop/authenticate/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('gameshop:index')
