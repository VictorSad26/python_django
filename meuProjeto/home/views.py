from django.shortcuts import redirect, render
from django.contrib.auth.views import LogoutView


def home(request):
    return render(request, "home.html")
