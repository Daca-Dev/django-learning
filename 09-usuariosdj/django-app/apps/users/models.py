from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Model definition for User."""
    
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )
    
    username = models.CharField('username', max_length=10, unique=True)
    email = models.EmailField('email', unique=True)
    nombres = models.CharField('nombres', max_length=30, blank=True)
    apellidos = models.CharField('apelldios', max_length=30, blank=True)
    genero = models.CharField('genero', max_length=1, choices=GENDER_CHOICES, blank=True)
    
    codregistro = models.CharField('código registro', max_length=6, blank=True,)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField('usuario activo', default=False)
    
    USERNAME_FIELD = 'username'
    
    REQUIRED_FIELDS = ['email',]
    
    objects = UserManager()
    
    class Meta:
        """Meta definition for User."""

        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return f'{self.nombres} {self.apelldios}'

    def __str__(self):
        """Unicode representation of User."""
        return self.username
