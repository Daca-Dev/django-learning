from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """ Vista para la pagina de inicio """
    template_name = 'home/home.html'
