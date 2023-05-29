from django.shortcuts import render, get_object_or_404, redirect
from .models import Game
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import CreateUserForm, LoginForm
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


def login(request):
    my_form = LoginForm()
    return render(request, 'gameshop/authenticate/login.html', {'my_form': my_form})


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
