from django.db import models
from django.db.models.functions import Lower


class PrestamoManager(models.Manager):
    """ Procedimiendos para Prestamo """
    
    def libros_promedio_edades(self):
        resultado = self.filter(
            libro__id ='2'
        ).aggregate(
            promedio_edad=models.Avg('lector__edad')
        )
        
        return resultado

    def num_libros_prestados(self):
        resultado = self.values(
            'libro'
        ).annotate(
            num_prestados=models.Count('libro'),
            titulo=Lower('libro__titulo')
        )
        
        for r in resultado:
            print('='*20)
            print(r, r.num_prestados)
            
        return resultado