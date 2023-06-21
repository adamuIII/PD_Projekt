from django.shortcuts import render, get_object_or_404, redirect
from .models import Game
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import CreateUserForm, UserLoginForm, OTPVerificationForm
from django.contrib import messages
from django_otp.decorators import otp_required
from django_otp.forms import OTPAuthenticationForm
from django.utils.crypto import get_random_string
from django.core.mail import send_mail

def generate_otp_code():
    return get_random_string(length=6)

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
            user = form.save(commit=False)
            user.set_unusable_password()
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'konto założone dla ' + user)
            return redirect("gameshop:login")
    context = {'form': form}
    return render(request, 'gameshop/authenticate/register.html', context)


def game(request, slug):
    game = get_object_or_404(Game, slug=slug)
    return render(request, 'gameshop/game.html', {'game': game})

def userlogin(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                otp_code = generate_otp_code()
                subject = 'Kod weryfikacyjny OTP'
                message = f'Twój kod weryfikacyjny OTP to: {otp_code}'
                from_email = 'noreply@semycolon.com'
                recipient_list = ['adamrzepka484@gmail.com']
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)

                request.session['otp_code'] = otp_code

                return redirect('gameshop:otpa')
            else:
                messages.info(request, 'Login lub hasło błędne')
    else:
        form = UserLoginForm()
    return render(request, 'gameshop/authenticate/login.html', {'form': form})


def userlogout(request):
    logout(request)
    return redirect('gameshop:index')

def otpa(request):
    if request.method == 'POST':
        form = OTPVerificationForm(request.POST)
        if form.is_valid():
            otp_code = form.cleaned_data['otp_code']
            stored_otp_code = request.session.get('otp_code')
            print(otp_code)
            print(stored_otp_code)
            if otp_code == stored_otp_code:
                # Kod OTP jest poprawny
                del request.session['otp_code']  # Usuń kod OTP z sesji po weryfikacji
                # Zaimplementuj dalsze działania po pomyślnej weryfikacji
                messages.success(request, 'Weryfikacja kodu OTP przebiegła pomyślnie.')
                return redirect('gameshop:index')
            else:
                # Kod OTP jest niepoprawny
                messages.error(request, 'Podany kod OTP jest niepoprawny.')
    else:
        form = OTPVerificationForm()

    return render(request, 'gameshop/authenticate/otpa.html', {'form': form})