
from PIL import Image

from django.db import models
from django.db.models.signals import post_save

from applications.autor.models import Autor
from .managers import LibroManager, CategoriaManager


class Categoria(models.Model):
    nombre = models.CharField('categoria', max_length=30)
    
    objects = CategoriaManager()

    class Meta:
        verbose_name = ("Categoria")
        verbose_name_plural = ("Categorias")

    def __str__(self):
        return f'{self.id}-{self.nombre}'


class Libro(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria_libro')
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField('titulo', max_length=50)
    fecha = models.DateTimeField('fecha de lanzamiento', auto_now=False, auto_now_add=False)
    portada = models.ImageField('portada', upload_to='portada', blank=True, null=True)
    visitas = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)
    
    objects = LibroManager()

    class Meta:
        verbose_name = ("Libro") # nombre en el admin
        verbose_name_plural = ("Libros") # nombre en plural del admin
        ordering = ['titulo', 'fecha'] # en que forma se organizarán

    def __str__(self):
        return f'{self.id}-{self.titulo.capitalize()}'
    
def optimize_image(sender, instance, **kwargs):
    if instance.portada:
        portada = Image.open(instance.portada.path)
        portada.save(instance.portada.path, quality=20, optimize=True)

post_save.connect(optimize_image, sender=Libro)