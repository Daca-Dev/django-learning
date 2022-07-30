from django.shortcuts import render
from django.views.generic.edit import FormView


from .forms import NewDepartamentoForm
from .models import Departamento
from applications.persona.models import Empleado

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '.'
    
    
    def form_valid(self, form):
        
        departamento = Departamento(
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['short_name'],
        )
        departamento.save()
        
        Empleado.objects.create(
            first_name=form.cleaned_data['nombre'],
            last_name=form.cleaned_data['apellido'],
            job='1',
            departament=departamento
        )
        
        return super(NewDepartamentoView, self).form_valid(form)
