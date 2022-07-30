
# Django
from applications.persona.admin import EmpleadoAdmin
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView, TemplateView,
    UpdateView, DeleteView
)
# models
from .models import Empleado


# 1. listar todos los empleados de la emrpesa GENERAL
class ListAllEmpleados(ListView):
    # con solo estos dos parametros ya serviria
    template_name = 'persona/list_all.html'
    model = Empleado
    # Paginación
    paginate_by = 4
    # context_object_name = 'lista'

# 2. listar todos los empleadoe que pertenece a un area de la empresa
class ListByAreaEmpleado(ListView):
    template_name = 'persona/list_by_area.html'
    model = Empleado

    def get_queryset(self):
        area = self.kwargs['departament']
        
        lista_query = Empleado.objects.filter(
            departament__short_name=area
        )
        return lista_query

# 3. Listar empleados por trabajo
class ListEmpleadoByKeyword(ListView):
    """ lista de empelados por palabra clave """
    
    template_name = 'persona/by_keyword.html'
    model = Empleado
    context_object_name = 'empleados'
    
    def get_queryset(self):
        print(''.center(20,'*'))
        palabra_clave = self.request.GET.get('kword', '')
        print(''.center(6, '='), palabra_clave)
        
        queryset = Empleado.objects.filter(
            first_name=palabra_clave
        )
        
        print(''.center(6, '+'), queryset)
        
        return queryset

# 5. Listar habilidades de un empleado
class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'
    
    def get_queryset(self):
        empleado = Empleado.objects.get(id='8')
        print(empleado.habilities.all())
        
        return empleado.habilities.all()
    
    

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"



class successView(TemplateView):
    template_name = "persona/success.html"



class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/create_empleado.html"
    fields = ['first_name', 'last_name', 'job', 'habilities', 'departament']
    # fields = ('__all__')
    success_url = reverse_lazy('persona_app:exito') # misma pagina
    
    def form_valid(self, form):
        
        empleado = form.save(commit=False) # crea la instancia de DB pero no guarda en DB
        empleado.full_name = f'{empleado.first_name} {empleado.last_name}'
        empleado.save()
        
        return super(EmpleadoCreateView, self).form_valid(form)
    
    

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update_empleado.html"
    success_url = reverse_lazy("persona_app:exito")
    # fields = ('__all__')
    fields = [
        'first_name',
        'last_name',
        'job',
        'departament',
        'habilities'
    ]

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy("persona_app:exito")
