from django.db import models

from .managers import AutorManager


class Persona(models.Model):
    nombres = models.CharField('nombre', max_length=50)
    apellidos = models.CharField('apellido', max_length=50)
    nacionalidad = models.CharField('nacionalidad', max_length=20)
    edad = models.PositiveIntegerField(default=0)
    class Meta:
        abstract = True
    
    def __str__(self) -> str:
        return f'{self.nombres} {self.apellidos}'


class Autor(Persona):
    
    seudonimo = models.CharField('seudonimo', max_length=50, blank=True, null=True)
    
    objects = AutorManager()