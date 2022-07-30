
from django.urls import path

from . import views


urlpatterns = [
    path(r'', views.HomeView.as_view()),
]
