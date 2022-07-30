from django.urls import path

from . import views


app_name = 'persona_app'

urlpatterns = [
    path('personas/', views.ListaPersona.as_view(), name='personas'),
    path('api/persons/list', views.ListaPersonaAPI.as_view(), name='personas-listar'),
    path('api/persons/list-pagination', views.ListaPersonaPaginacionAPI.as_view(), name='personas-listar-pag'),
    path('api/persons/list-simple', views.ListaPersonaSimpleAPI.as_view(), name='personas-listar'),
    path('api/persons/create', views.CrearPersonaAPI.as_view(), name='personas-crear'),
    path('api/persons/detail/<pk>', views.DetallePersonaAPI.as_view(), name='personas-detail'),
    path('api/persons/delete/<pk>', views.BorrarPersonaAPI.as_view(), name='personas-delete'),
    path('api/persons/update/<pk>', views.ActualizarPersonAPI.as_view(), name='personas-update'),
    path('api/persons/modified/<pk>', views.ActualizarDetallarPersonAPI.as_view(), name='personas-update-detail'),
    
    path('api/reuniones/list', views.ReunionListaAPI.as_view(), name='reunion-list'),
    path('api/reuniones/list-link', views.ReunionListaLinkAPI.as_view(), name='reunion-list-link'),
]