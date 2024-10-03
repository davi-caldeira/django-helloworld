from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse(f"<h1>Hello {nome}, de {int(idade)} anos</h1>")

def soma(request, n1, n2):
    return HttpResponse(f"<h1>Soma: {int(n1) + int(n2)}</h1>")

def sub(request, n1, n2):
    return HttpResponse(f"<h1>Subtração: {int(n1) - int(n2)}</h1>")

def mult(request, n1, n2):
    return HttpResponse(f"<h1>Multiplicação: {int(n1) * int(n2)}</h1>")

def div(request, n1, n2):
    return HttpResponse(f"<h1>Divisão: {int(n1) / int(n2)}</h1>")