from datetime import date

from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect

from .models import Prestamo
from .forms import PrestamoForm, MultiplePrestamoForm

class RegistrarPrestamo(FormView):
    template_name = 'lector/add-prestamo.html'
    form_class = PrestamoForm
    success_url = '.' # la misma página
    
    def form_valid(self, form):
        
        # Prestamo.objects.create(
        #     lector=form.cleaned_data['lector'],
        #     libro=form.cleaned_data['libro'],
        #     fecha_prestamo=date.today(),
        #     devuelto=False
        # )
        
        prestamo = Prestamo(
            lector=form.cleaned_data['lector'],
            libro=form.cleaned_data['libro'],
            fecha_prestamo=date.today(),
            devuelto=False    
        )
        prestamo.save()
        
        libro = form.cleaned_data['libro']
        libro.stock -= 1
        libro.save()
        
        return super(RegistrarPrestamo, self).form_valid(form)



class AddPrestamo(FormView):
    template_name = 'lector/add-prestamo.html'
    form_class = PrestamoForm
    success_url = '.' # la misma página
    
    def form_valid(self, form):
        
        obj, created = Prestamo.objects.get_or_create(
            # especificar en base a que esta creado
            lector=form.cleaned_data['lector'],
            libro=form.cleaned_data['libro'],
            devuelto=False,
            # si no existe tomara estos valores adicionales para crearlo
            defaults= {
                'fecha_prestamo': date.today(),
            }
        )
        
        if created:
            return super(AddPrestamo, self).form_valid(form)
        else:
            return HttpResponseRedirect('/')


class AddMultiplePrestamo(FormView):
    template_name = 'lector/add-multiple-prestamo.html'
    form_class = MultiplePrestamoForm
    success_url = '.' # la misma página
    
    def form_valid(self, form):
        
        prestamos = []
        
        for libro in form.cleaned_data['libros']:
            prestamo = Prestamo(
                lector=form.cleaned_data['lector'],
                libro=libro,
                fecha_prestamo=date.today(),
                devuelto=False    
            )
            prestamos.append(prestamo)

        Prestamo.objects.bulk_create(prestamos)
        
        return super(AddMultiplePrestamo, self).form_valid(form)