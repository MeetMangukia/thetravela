from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('hotel-list/', views.hotel_list, name="hotel_list"),
    path('tour-list/', views.tour_list, name="tour_list"),
    path('car-list/', views.car_list, name="car_list"),

    path('hotel-page/<int:hotel_id>', views.hotel_page, name="hotel_page"),
    path('tour-page/<int:tour_id>', views.tour_page, name="tour_page"),
    path('car-page/', views.car_page, name="car_page"),
]