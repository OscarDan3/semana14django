from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template,Context
from django.template import loader


def incio(request):
    return  render(request, 'inicio.html')
   
def servico(request):
    return render(request, 'servicio.html')


def des(request):
    return render(request, 'descripcion.html')
    