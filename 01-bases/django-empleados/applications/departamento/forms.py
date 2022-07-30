
from django import forms



class NewDepartamentoForm(forms.Form):
    nombre = forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=60)
    
    short_name = forms.CharField(max_length=60)
    departamento = forms.CharField(max_length=60)