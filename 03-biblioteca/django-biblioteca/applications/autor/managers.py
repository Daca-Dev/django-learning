
from django.db import models
from django.db.models import Q


class AutorManager(models.Manager):
    """ managaers para el modelo autor """
    
    def listar_autores(self):
        return self.all()
    
    def buscar_autor(self, kword):
        resultado = self.filter(
            nombre__icontains=kword
        )
        return resultado
        
    def buscar_autor_2(self, kword):
        resultado = self.filter(
            Q(nombre__icontains=kword) | Q(apellido__icontains=kword)
        )
        return resultado
    
    def buscar_autor_3(self, kword):
        resultado = self.filter(
            nombre__icontains=kword
        ).exclude(
            Q(edad=26) | Q(edad=25)
        )
        
        return resultado
    
    def buscar_autor_4(self, kword):
        resultado = self.filter(
            edad__gt=23,
            edad__lt=25
        ).order_by('apellido', 'nombre', 'id')
        
        return resultado
