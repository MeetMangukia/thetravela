from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Hotel, Tour, Car

def hotel_list(request):
    if request.method == 'POST':
        city = request.POST['city']
        hotels = Hotel.objects.filter(city__contains=city)
        context = {
            'hotels': hotels
        }          
        return render(request, "listing/hotel-list.html", context)

    hotels = Hotel.objects.all()
    context = {
        'hotels': hotels
    }
    return render(request, "listing/hotel-list.html", context)

def tour_list(request):
    tours = Tour.objects.all()
    context = {
        'tours': tours
    }
    return render(request, "listing/tour-list.html", context)

def car_list(request):
    if request.method == 'POST':
        members = request.POST['members']
        if members == '4' or members == '7':
            cars = Car.objects.filter(members=members)
            context = {
                'cars': cars
            }          
            return render(request, "listing/car-list.html", context)
    cars = Car.objects.all()
    context  = {
        'cars': cars
    }
    return render(request, "listing/car-list.html", context)


def hotel_page(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    context = {
        'hotel': hotel
    }
    return render(request, "listing/hotel-page.html", context)

def tour_page(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id)
    context = {
        'tour': tour
    }
    return render(request, "listing/tour-page.html", context)

def car_page(request):
    return render(request, "listing/car-page.html")