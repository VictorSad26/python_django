from django.shortcuts import get_object_or_404, redirect, render
from .models import Cliente
from .forms import ClienteForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def person_list(request):
    clientes = Cliente.objects.filter(user=request.user)
    return render(request, "clientes.html", {"clientes": clientes})


@login_required
def person_new(request):
    form = ClienteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        cliente = form.save(commit=False)
        cliente.user = request.user
        cliente.save()  # Salva no banco de dados
        return redirect("person_list")
    return render(request, "form_cliente.html", {"form": form})


@login_required
def person_update(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect("person_list")
    return render(request, "form_cliente.html", {"form": form})


@login_required
def person_delete(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    if request.method == "POST":
        cliente.delete()
        return redirect("person_list")
    return render(request, "confirm_delete.html", {"cliente": cliente})
