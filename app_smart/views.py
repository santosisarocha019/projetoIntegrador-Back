from django.shortcuts import render
from django.http import HttpResponse

def abre_index(request):
    mensagem = "olá muito bom dia"
    return HttpResponse(mensagem)