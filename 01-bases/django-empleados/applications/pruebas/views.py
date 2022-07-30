# Dajngo
from django.shortcuts import render
from django.views.generic import (
    TemplateView, ListView, CreateView
)
# Local
from applications.pruebas.forms import PruebaForm
from . import models

class PruebaView(TemplateView):
    """ Vista generica de pruebas 
    Especificamos los parametros para configurar la Clase de la que heredamos (TemplateView)
    """
    template_name = 'pruebas/prueba.html' # hacemos referencia a un arhcivo HTML
    


class PruebaListView(ListView):
    template_name = "pruebas/lista.html"
    context_object_name = 'listaNumeros'
    queryset = ['0', '10', '20', '30']


class ListarPrueba(ListView):
    """ Vista para mostrar el uso de templates con DB """
    template_name = "pruebas/lista_prueba.html"
    model = models.Prueba
    context_object_name = 'lista'
    

class CrearPrueba(CreateView):
    """ Prueba de la vista CreateView con el modelo Prueba """
    template_name = 'pruebas/add.html'
    model = models.Prueba
    form_class = PruebaForm
    success_url = '.'