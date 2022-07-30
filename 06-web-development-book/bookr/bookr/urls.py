from django.contrib import admin
from django.urls import path

from reviews import views as reviews_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', reviews_views.index),
    path('book-search/', reviews_views.search),
]
