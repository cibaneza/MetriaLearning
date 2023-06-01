from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path("x", views.home, name="x"),
    path("agradecimientos", views.agradecimientos, name="agradecimientos"),
    path("nosotros", views.nosotros, name="nosotros"),
    path("", views.ejemplo, name="home"),
]
