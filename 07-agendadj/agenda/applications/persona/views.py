from django.shortcuts import render
from django.views.generic import (
    ListView
)

from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveAPIView, # RetrieveAPIView == DetailView
    DestroyAPIView, UpdateAPIView, RetrieveUpdateAPIView
)

from .models import Person, Reunion
from .serializers import (
    PersonaSerializer, PersonaSerializerSimple, PersonaSerializerAddFields,
    ReunionSerializer, ReunionSerializerLink, PersonaPaginacion
)


# View
class ListaPersona(ListView):
    template_name = 'persona/personas.html'
    context_object_name = 'personas'

    def get_queryset(self):
        return Person.objects.all()
    
# REST
class ListaPersonaAPI(ListAPIView):
    
    serializer_class = PersonaSerializer
    
    def get_queryset(self):
        return Person.objects.all()
    
class ListaPersonaPaginacionAPI(ListAPIView):
    
    serializer_class = PersonaSerializer
    pagination_class = PersonaPaginacion
    
    def get_queryset(self):
        return Person.objects.all()
    
class ListaPersonaSimpleAPI(ListAPIView):
    
    serializer_class = PersonaSerializerAddFields
    
    def get_queryset(self):
        return Person.objects.all()

class CrearPersonaAPI(CreateAPIView):
    """ Vista para crear un registro del modelo Persona """
    serializer_class = PersonaSerializer
    
    
class DetallePersonaAPI(RetrieveAPIView):
    """ Vista API para detallar un registro del modelo Persona """
    serializer_class = PersonaSerializer
    queryset = Person.objects.all() # query de donde buscara el registro buscado
    
class BorrarPersonaAPI(DestroyAPIView):
    """ Vista API para eliminar un registro del modelo Persona """
    # necesita del metodo HTTP DELETE
    serializer_class = PersonaSerializer
    queryset = Person.objects.all() # query de donde buscara el registro buscado
    
class ActualizarPersonAPI(UpdateAPIView):
    """ Vista API para actualizar datos con del modelo Persona"""
    serializer_class = PersonaSerializer
    queryset = Person.objects.all()
    
class ActualizarDetallarPersonAPI(RetrieveUpdateAPIView):
    """ Vista API para actualizar datos con del modelo Persona"""
    serializer_class = PersonaSerializer
    queryset = Person.objects.all()
    
    
class ReunionListaAPI(ListAPIView):
    """ vista API apra el modelo reunion """
    serializer_class = ReunionSerializer
    def get_queryset(self):
        return Reunion.objects.all()
    
    
class ReunionListaLinkAPI(ListAPIView):
    """ vista API apra el modelo reunion """
    serializer_class = ReunionSerializerLink
    
    def get_queryset(self):
        return Reunion.objects.all()
    