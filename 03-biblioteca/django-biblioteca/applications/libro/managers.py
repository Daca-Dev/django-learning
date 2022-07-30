
from django.db import models
from django.contrib.postgres.search import TrigramSimilarity

from datetime import datetime


class LibroManager(models.Manager):
    """ managaers para el modelo autor """
    
    def listar_libros(self, kword):
        return self.filter(
            titulo__icontains=kword,
        )
    
    def listar_libros_trg(self, kword):
        
        if kword:
            return self.filter(
                titulo__trigram_similar=kword,
            )
        else:
            return self.all()[:10]
    
    def listar_libros_2(self, kword, date_init, date_end):
        
        date_1 = datetime.strptime(date_init, r"%Y-%m-%d").date()
        date_2 = datetime.strptime(date_end, r"%Y-%m-%d").date()
        
        return self.filter(
            titulo__contains=kword,
            fecha__range=(date_1, date_2)
        )

    def listar_libros_categoria(self, categoria):
        return self.filter(
            categoria__id=categoria
        ).order_by('titulo')
        
    def add_autor_libro(self, libro_id, autor_id):
        libro = self.get(id=libro_id)
        libro.autores.add(autor_id) # parametro many to many
        return libro
    
    def libros_num_prestados(self):
        """ """
        resultado = self.aggregate(
            num_prestados=models.Count('libro_prestamo')
        )
        return resultado


class CategoriaManager(models.Manager):
    """ Managers para el modelo autor """
    
    def categoria_por_autor(self, autor):
        return self.filter(
            categoria_libro__autores__id=autor
        ).distinct() # distinct solo trae las consultas que no se repiten
        
    def listar_categoria_libros(self):
        """ obtiene un conteo de los libros por categoria """
        
        # annotate nos sirve apra generar nuevos campos en nuestro resultado
        resultado = self.annotate(
            num_libros=models.Count('categoria_libro') 
        )
        
        for r in resultado:
            print(r, r.num_libros)
        
        return resultado
    
    def num_libros_prestados(self):
        resultado = self.annotate(
            num_prestados=models.Count('libro_presamo')
        )
        
        for r in resultado:
            print('='*20)
            print(r, r.num_prestados)
            
        return resultado
