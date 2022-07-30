from django.contrib import admin

from .models import Libro, Categoria


admin.site.register(Libro)
admin.site.register(Categoria)
