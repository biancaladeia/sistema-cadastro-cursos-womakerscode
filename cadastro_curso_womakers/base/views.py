from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return HttpResponse("Olá, mundo. Você está na página inicial do projeto womakerscode!")

def cadastro(request):
    pass

