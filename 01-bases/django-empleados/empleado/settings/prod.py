"""
Configuraciones para cuando la app este alojada en un servidor
"""
from ._base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'dacacode',
        'PASSWORD': 'dacacodecursopro',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}