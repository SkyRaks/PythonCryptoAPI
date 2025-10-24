from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
import requests
# from requests import Session
import json
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

# i'm using CoinMarketCap API
# put your own api key
api_key = "your api key"
base_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

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

def get_crypto_data():
    parameters = {
        'start': '1',
        'limit': '10',
        'convert': 'USD'
    }

    headers = {
        'Content-Type': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    try:
        responce = requests.get(url=base_url, headers=headers, params=parameters)
        data =responce.json()
        crypto_data = data.get("data", [])
        print(f"status code: {responce.status_code}")
        return crypto_data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        crypto_data = []
        print(e)
    return crypto_data
