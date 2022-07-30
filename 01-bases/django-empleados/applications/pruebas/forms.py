# Django
from django import forms
from django.forms import widgets
# Local
from .models import Prueba

class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
        )
        
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form__input',
                'placeholder': 'Ingresa el titulo..'
            })
        }
        
    
    def clean_cantidad(self):
        """ Validador para el campo de cantidad """
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('El valor de cantidad debe ser menor a 10')
        
        return cantidad