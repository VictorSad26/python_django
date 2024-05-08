from django.shortcuts import get_object_or_404, redirect, render
from .models import Cliente
from .forms import ClienteForm

# Create your views here.


def person_list(request):
    clientes = Cliente.objects.all()
    return render(request, "clientes.html", {"clientes": clientes})


def person_new(request):
    form = ClienteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()  # Salva no banco de dados
        return redirect("person_list")
    return render(request, "form_cliente.html", {"form": form})


def person_update(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect("person_list")
    return render(request, "form_cliente.html", {"form": form})


def person_delete(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    if request.method == "POST":
        cliente.delete()
        return redirect("person_list")
    return render(request, "confirm_delete.html", {"cliente": cliente})
