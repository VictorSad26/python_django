from django.shortcuts import get_object_or_404, redirect, render
from .models import Cliente
from .forms import ClienteForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
        messages.success(request, "Cliente cadastrado com sucesso!")
        return redirect("person_list")
    return render(request, "form_cliente.html", {"form": form})


@login_required
def person_update(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    form = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect("person_list")
    else:
        messages.error(
            request, "O cliente não foi atualizado. Por favor, corrija os erros."
        )
    return render(request, "clientes.html", {"form": form, "cliente": cliente})


@login_required
def person_delete(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    if request.method == "POST":
        cliente.delete()
        return redirect("person_list")
    return render(request, "clientes.html", {"cliente": cliente})
