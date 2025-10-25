from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from website.scripts import get_crypto_data
from .models import Portfolio

# i'm using CoinMarketCap API
# put your own api key

# Create your views here.
def home(request):
    crypto_data = get_crypto_data()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "you have been logged in")
            return redirect('home')
        else:
            messages.success(request, "error try again")
            return redirect('home')
    else:
        return render(request, 'home.html', {'crypto_data': crypto_data})

def logout_user(request):
    logout(request)
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect('home')
    else:
        return render(request, 'register.html')

def user_profile(request):
    if request.user.is_authenticated:
        user_id = request.user
        portfolio = Portfolio.objects.filter(user_id_id=user_id)
        return render(request, 'user_profile.html', {'portfolio':portfolio})
    else:
        messages.success(request, "You have to be logged in to view that page!")
        return redirect('home')

def purchase_coin(request, coin, price):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # name = request.POST[coin]
            amount = request.POST.get('amount')
            portfolio = Portfolio.objects.create(user_id=request.user, name=coin, amount=amount, price=price)
            portfolio.save()
            return redirect('home')
        else:
            # GET request
            print(price)
            return render(request, 'purchase_coin.html', {'coin':coin, 'price':price})

    else:
        return redirect('home')

