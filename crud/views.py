from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Carro

# Crear la vista principal
def index(request):
    lista_carros = Carro.objects.all()  

    context = {
        'carros': lista_carros 
    }

    template = loader.get_template("index.html")

    return HttpResponse(template.render(context, request))

# Vista para el detalle
def vista_detalle(request, id_carro):
    detalle_carro = Carro.objects.get(id=id_carro)
    
    template = loader.get_template("detail.html")
    
    context = {'carro': detalle_carro}
    
    return HttpResponse(template.render(context, request))