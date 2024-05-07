from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return render(request, "index.html")


def lerDoBanco(nome):
    lista_nomes = [
        {"nome": "Ana", "idade": 20},
        {"nome": "Pedro", "idade": 25},
        {"nome": "Maria", "idade": 30},
    ]
    for pessoa in lista_nomes:
        if pessoa["nome"] == nome:
            return pessoa
        else:
            return {"nome": "Pessoa não encontrada"}


def pegarDados(request, nome):
    resultado = lerDoBanco(nome)
    if resultado["nome"] != nome:
        return render(request, "pessoa.html", {"v_resultado": "Pessoa não encontrada"})
    else:
        return render(
            request,
            "pessoa.html",
            {"v_resultado": f"Nome: {resultado['nome']} Idade: {resultado['idade']}"},
        )
        # return render(f"Nome: {resultado['nome']} Idade: {resultado['idade']}")
