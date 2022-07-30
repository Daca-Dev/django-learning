
# Dango
from django.db import models
# External apps
from ckeditor.fields import RichTextField
# Local
from applications.departamento import models as dept_models


class Habilidades(models.Model):
    """ Modelo de habilidades para cada empleado """
    habilidad = models.CharField('habilidad', max_length=50)
    
    class Meta:
        verbose_name = 'habilidad'
        verbose_name_plural = 'habilidades'
        
    def __str__(self):
        return self.habilidad
    


class Empleado(models.Model):
    """ modelo para la tabla empleado """
    
    JOB_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'otro'),
    )
    
    first_name = models.CharField('nombre', max_length=60)
    last_name = models.CharField('apellido', max_length=60)
    job = models.CharField('trabajo', max_length=1, choices=JOB_CHOICES)
    
    full_name = models.CharField('nombre completo', max_length=120, blank=True)
    
    habilities = models.ManyToManyField(Habilidades)
    departament = models.ForeignKey(dept_models.Departamento, on_delete=models.CASCADE)
    
    hoja_vida = RichTextField()
    
    # image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)
    
    class Meta:
        verbose_name = 'empleado'
        verbose_name_plural = 'empleados'
        ordering = ['first_name', 'last_name']
        unique_together = ('first_name', 'last_name', 'departament')
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
