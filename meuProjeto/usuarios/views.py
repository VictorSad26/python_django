from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def create_superuser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        User.objects.create_superuser(username=username, password=password, email=email)
        return redirect("login")
    else:
        return render(request, "cadastro.html")
