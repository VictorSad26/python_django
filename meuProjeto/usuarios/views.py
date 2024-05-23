import re
from django.forms import ValidationError
from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.validators import validate_email


def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    return True


def create_superuser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]

        if not email:
            messages.error(request, "O email é obrigatório.")
            return render(request, "cadastro.html")

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Email inválido.")
            return render(request, "cadastro.html")

        if not email.endswith(("@gmail.com", "@outlook.com", "@hotmail.com")):
            messages.error(
                request,
                "O email deve ser do domínio @gmail.com, @outlook.com ou @hotmail.com.",
            )
            return render(request, "cadastro.html")

        if " " in username:
            messages.error(request, "O nome de usuário não pode conter espaços.")
            return render(request, "cadastro.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Nome de usuário já está em uso.")
            return render(request, "cadastro.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email já está em uso.")
            return render(request, "cadastro.html")

        if not password:
            messages.error(request, "A senha é obrigatória.")
            return render(request, "cadastro.html")

        if not validate_password(password):
            messages.error(
                request,
                "A senha deve ter pelo menos 8 caracteres, incluir um número e uma letra maiúscula.",
            )
            return render(request, "cadastro.html")

        User.objects.create_superuser(username=username, password=password, email=email)
        return redirect("login")
    else:
        return render(request, "cadastro.html")
