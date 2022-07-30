from django import forms
from django.contrib.auth import authenticate

from .models import User

class UserRegisterForm(forms.ModelForm):
    """Form definition for UserRegister."""
    
    password_1 = forms.CharField(
        label='contraseña',
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'contraseña'
        })
    )
    
    password_2 = forms.CharField(
        label='contraseña',
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'repetir contraseña'
        })
    )

    class Meta:
        """Meta definition for UserRegisterform."""

        model = User
        fields = (
            'username', 'email', 'nombres', 'apellidos',
            'genero'
        )

    def clean_password_1(self):
        if len(self.cleaned_data.get("password_1")) <= 6:
            self.add_error('password_1', 'la contraseña es menor de 6 caracteres')
        
        if self.cleaned_data.get("password_1") != self.cleaned_data.get("password_2"):
            self.add_error('password_1', 'las contraseñas no son la misma')

class LoginForm(forms.Form):
    
    username = forms.CharField(
        label='username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'username',
                'style': r'{margin: 10px}'
            }
        )
    )
    password = forms.CharField(
        label='contraseña',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'contraseña',
                'style': r'{margin: 10px}'
            }
        )
    )
    # validación general
    def clean(self):
        super(LoginForm, self).clean()
        
        if not authenticate(
            username = self.cleaned_data.get("username"),
            password = self.cleaned_data.get("password")
        ):
            raise forms.ValidationError('los datos de usuario no son correctos')
        
        return self.cleaned_data
    

class UpdatePasswordForm(forms.Form):
    """UpdatePasswordForm definition."""

    password_1 = forms.CharField(
        label='contraseña Actual',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'contraseña Actual',
                'style': r'{margin: 10px}',
                'type': 'password',
            }
        )
    )

    password_2 = forms.CharField(
        label='contraseña Nueva',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'contraseña Nueva',
                'style': r'{margin: 10px}',
                'type': 'password',
            }
        )
    )


class VerificationForm(forms.Form):
    """ """
    codregistro = forms.CharField(required=True)
    
    def __init__(self, pk, *args, **kwargs):
        self.id_user = pk
        super(VerificationForm, self).__init__(*args, **kwargs)
    
    def clean(self):
        
        codigo = self.cleaned_data['codregistro']
        
        if len(codigo) == 6:
            # verificamos si el codigo y el id de usuario son validos
            activo = User.objects.code_validation(
                self.id_user,
                codigo
            )
            if not activo:
                raise forms.ValidationError('El código es incorrecto')                
        else:
            raise forms.ValidationError('El código es incorrecto')

            
        return super().clean()
    