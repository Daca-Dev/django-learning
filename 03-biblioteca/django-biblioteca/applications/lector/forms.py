from applications.autor.models import Persona
from django import forms

from .models import Prestamo
from applications.libro.models import Libro


class PrestamoForm(forms.ModelForm):
    """PrestamoForm definition."""

    class Meta:
        model = Prestamo
        fields = ('libro', 'lector')


class MultiplePrestamoForm(forms.ModelForm):
    """Form definition for MiltiplePrestamoForm."""

    libros = forms.ModelMultipleChoiceField(
        # valores del input
        queryset=None,
        required=True,
        # widgets de ese input
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        """Meta definition for MiltiplePrestamoFormform."""

        model = Prestamo
        fields = (
            'lector',
        )

    def __init__(self, *args, **kwargs):
        super(MultiplePrestamoForm, self).__init__(*args, **kwargs)
        self.fields['libros'].queryset = Libro.objects.all()
