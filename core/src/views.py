from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html")


def shop(request):
    return render(request, "pages/shop.html")

# Create your views here.
