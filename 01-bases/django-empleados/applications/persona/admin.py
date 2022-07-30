from django.contrib import admin
# local
from . import models

admin.site.register(models.Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'first_name', 'last_name', 'job', 'departament',
        # campo para un funcion especial
        'full_name', 'full_name_funct',
    )
    search_fields = (
        'first_name', 'last_name',
    )
    list_filter = (
        'job', 'habilities', 'departament'
    )
    # este aprametro solo funciona con campos muchos a muchos
    filter_horizontal = ('habilities',)
    
    # funciones especiales
    def full_name_funct(self, obj):
        """ Función para generar el campo full_name """
        print(obj) # obj es cada objeto que trae
        return f'{obj.first_name} {obj.last_name}'

admin.site.register(models.Empleado, EmpleadoAdmin)