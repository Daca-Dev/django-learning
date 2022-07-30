from django.db.models import fields
from rest_framework import serializers, pagination
from rest_framework.utils import field_mapping

from .models import Person, Reunion, Hobby


class HobbySerializer(serializers.ModelSerializer):
    """ Serializador para el modelo Hobby """
    class Meta:
        model = Hobby
        fields = ('id', 'hobby')


class PersonaSerializer(serializers.ModelSerializer):
    """ Serializer for model Person """
    hobbies = HobbySerializer(many=True)
    class Meta:
        model = Person
        fields = ('id', 'full_name', 'email', 'phone', 'hobbies')
        
class PersonaPaginacion(pagination.PageNumberPagination):
    """ Serializador de persona para crear una paginación """
    page_size = 2
    max_page_size = 5


class PersonaSerializerSimple(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    active = serializers.BooleanField(required=False)


class PersonaSerializerAddFields(serializers.ModelSerializer):
    """ Serializer for model Person """
    active = serializers.BooleanField(default=False)

    class Meta:
        model = Person
        fields = ('__all__')


class ReunionSerializer(serializers.ModelSerializer):

    persona = PersonaSerializer()
    fecha_completa = serializers.SerializerMethodField()

    class Meta:
        model = Reunion
        fields = (
            'id', 'fecha', 'hora',
            'asunto', 'persona','fecha_completa'
        )
        
    def get_fecha_completa(self, obj):
        return f'{str(obj.fecha)} - {str(obj.hora)}'


class ReunionSerializerLink(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reunion
        fields = (
            'id', 'fecha', 'hora',
            'asunto', 'persona'
        )
        
        extra_kwargs = {
            'persona': {'view_name': 'persona_app:personas-detail', 'lookup_field': 'pk'}
        }