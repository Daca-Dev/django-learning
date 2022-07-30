"""
Rutas de la aplicación home
"""
# Django
from django.urls import path
# Local app
from . import views


urlpatterns = [
    path( 'prueba/', views.PruebaView.as_view() ), # el metodo as_view() le dice a Django que vamos a usar una vista basada en clases
    path( 'lista/', views.PruebaListView.as_view() ), # el metodo as_view() le dice a Django que vamos a usar una vista basada en clases
    path( 'lista-prueba/', views.ListarPrueba.as_view() ), 
    path( 'add/', views.CrearPrueba.as_view() ), 
]
