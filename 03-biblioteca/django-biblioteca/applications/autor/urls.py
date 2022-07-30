from django.urls import path

from . import views


urlpatterns = [
    path(
        'autores/',
        views.ListAutores.as_view(),
        name='autores'
    ),
]
