from django.db import models


class Departamento(models.Model):
    """ modelo para los Departamentos """
    name = models.CharField('nombre' ,max_length=50)
    short_name = models.CharField('nombre corto' ,max_length=20)
    anulate = models.BooleanField('anulado', default=False)
    
    class Meta:
        verbose_name = 'departamento'
        verbose_name_plural = 'departamentos'
        ordering = ['-name']
        unique_together = ('name', 'short_name')
    
    def __str__(self):
        return f'{self.name} - active: {self.anulate}'
    