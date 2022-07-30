from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Libro


class ListLibros(ListView):
    template_name = "libro/lista.html"
    context_object_name = 'lista_libros'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        date_init = self.request.GET.get('date', '')
        date_end = self.request.GET.get('date_1', '')

        print(date_end)
        print(date_init)

        if date_init and date_end:
            return Libro.objects.listar_libros_2(palabra_clave, date_init, date_end)
        else:
            return Libro.objects.listar_libros(palabra_clave)


class ListLibrosTrg(ListView):
    template_name = "libro/lista.html"
    context_object_name = 'lista_libros'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        
        return Libro.objects.listar_libros_trg(palabra_clave)


class ListLibros2(ListView):
    template_name = "libro/lista2.html"
    context_object_name = 'lista_libros'

    def get_queryset(self):
        return Libro.objects.listar_libros_categoria(1)


class LibroDetailView(DetailView):
    model = Libro
    template_name = "libro/detalle.html"
