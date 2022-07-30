from django.db import models


class Prueba(models.Model):
    """ Modelo de prueba """
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    
    def __str__(self):
        return self.titulo
