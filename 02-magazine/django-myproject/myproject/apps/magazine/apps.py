"""
Magazine app configration
"""
# django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MagazineConfig(AppConfig):
    name = 'myproject.apps.magazine'
    verbose_name = _('Magazine')
    default_auto_field = 'django.db.models.BigAutoField'
    
    def ready(self):
        from . import signals
