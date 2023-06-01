from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def agradecimientos(request):
    return render(request, "agradecimientos.html")


def nosotros(request):
    return render(request, "nosotros.html")


def ejemplo(request):
    return render(request, "ejemplo.html")
