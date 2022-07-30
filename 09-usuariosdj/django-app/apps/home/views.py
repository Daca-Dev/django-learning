from datetime import datetime

from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView
)


# Construir mi propio mixin
class FechaMixin(object):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fecha'] = datetime.now()
        return context

# vistas    
class HomePage(LoginRequiredMixin, FechaMixin, TemplateView):
    template_name = "home/index.html"
    # Atributo para el LoginRequiredMixin
    login_url = reverse_lazy('users_app:user-login')
    
class TemplatePruebaMixin(FechaMixin, TemplateView):
    template_name = 'home/mixin.html'