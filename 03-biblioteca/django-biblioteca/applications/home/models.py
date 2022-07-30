from django.db import models


class Persona(models.Model):

    full_name = models.CharField('nombre completo', max_length=50)
    pais = models.CharField('país', max_length=30)
    pasaporte = models.CharField('pasaporte', max_length=50)
    edad = models.IntegerField('edad')
    apelativo = models.CharField('apelativo', max_length=10)
    

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        db_table = 'persona' # nombre de la tabla en la base de datos
        unique_together = ('pais', 'apelativo') # no quiero dos veces un registro con el mismo país y apelativo
        constraints = [
            models.CheckConstraint(check=models.Q(edad__gte=18), name='edad_mayor_18')
        ]
        abstract = True

    def __str__(self):
        return self.full_name


class Empleados(Persona):
    empleo = models.CharField('empleo', max_length=50)

class Cliente(Persona):
    email = models.CharField('email', max_length=90)