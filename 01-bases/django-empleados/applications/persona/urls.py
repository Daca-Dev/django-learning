"""
Rutas de la aplicación persona
"""

# Django
from django.urls import path
# Local
from . import views

app_name = 'persona_app'

urlpatterns = [
    path('listar-empleados/', views.ListAllEmpleados.as_view()),
    path('listar-por-area/<departament>/', views.ListByAreaEmpleado.as_view()),
    path('buscar-empleados/', views.ListEmpleadoByKeyword.as_view()),
    path('listar-habilidades-empleados/', views.ListHabilidadesEmpleado.as_view()),
    path('detalles-empleados/<pk>/', views.EmpleadoDetailView.as_view()),
    path('crear-empleado/', views.EmpleadoCreateView.as_view()),
    path('exito/', views.successView.as_view(), name='exito'),
    path('modificar-empleado/<pk>/', views.EmpleadoUpdateView.as_view(), name='modificar_empleado'),
    path('eliminar-empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name='eliminar_empleado'),
]
