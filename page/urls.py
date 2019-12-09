from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    path('signin/', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path('logout', views.logout, name="logout"),

    path('contact', views.contact, name="contact"),
    path('inquery-hotel/<int:hotel_id>', views.inquery_hotel, name="inquery_hotel"),
    path('inquery-tour/<int:tour_id>', views.inquery_tour, name="inquery_tour"),
    path('inquery-car/<int:car_id>', views.inquery_car, name="inquery_car"),

    path('replay', views.replay, name="replay"),
    path('payment/<int:amount>', views.payment, name="payment"),
    path('loading', views.loading, name="loading"),



]