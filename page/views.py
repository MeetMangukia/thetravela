from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from account.models import UserProfile
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from account.backends import EmailBackend
from django.contrib import messages, auth
from listing.models import Hotel, Tour, Car

def index(request):
    tours = Tour.objects.filter(is_hot=True)[:3]
    context = {
        'tours': tours
    }
    return render(request, "page/index.html", context)

def signin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)
        if user is not None:
            print("You are Logged in")
            auth.login(request, user)
            return redirect('index')
        else:
            print("please Enter Valid Email or Password")
    return render(request, "page/signin.html")

def signup(request):
    if request.method == "POST":
        if request.POST['form_type'] == 'register':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']

            User.objects.create_user(username, email, password)
            
            return render(request, "page/signin.html")
    return render(request, "page/signup.html")

def logout(request):
    auth.logout(request)
    print("Logged Out")
    return redirect('index')

def contact(request):
    return render(request, "page/contact.html")

def inquery_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    context = {
        'hotel': hotel
    }
    return render(request, "page/inquery-hotel.html", context)

def inquery_tour(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id)
    context = {
        'tour': tour
    }
    return render(request, "page/inquery-tour.html", context)

def inquery_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    context = {
        'car': car
    }
    return render(request, "page/inquery-car.html", context)

def replay(request):
    return render(request, "page/replay.html")

def payment(request, amount):
    context = {
        'amount': amount
    }
    return render(request, "page/payment.html", context)

def loading(request):
    return render(request, "page/loading.html")
