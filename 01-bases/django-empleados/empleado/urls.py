"""
URLs del archivo principal del proyecto
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # incluimos las URL's de las app's
    path(r'', include('applications.home.urls')),
    # path(r'', include('applications.departamento.urls')),
    # path(r'', include('applications.persona.urls')),
    # path(r'prueba/', include('applications.pruebas.urls'))
]
