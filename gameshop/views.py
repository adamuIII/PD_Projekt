from django.shortcuts import render, get_object_or_404
from .models import Game
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm


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
    form = CreateUserForm
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'gameshop/authenticate/register.html', context)


def game(request, slug):
    game = get_object_or_404(Game, slug=slug)
    return render(request, 'gameshop/game.html', {'game': game})
