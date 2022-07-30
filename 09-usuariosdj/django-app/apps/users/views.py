from django.http.response import HttpResponseRedirect
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.urls.base import reverse
from django.views.generic import (
    View,
    CreateView,
)
from django.views.generic.edit import (
    FormView,
)

from .models import User
from .forms import UserRegisterForm, LoginForm, UpdatePasswordForm, VerificationForm
from .functions import code_generator

# REGISTAR UN NUEVO USUARIO
class UserRegisterView(FormView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = '/' # url de raíz
    
    def form_valid(self, form):
        # generamos el código
        code = code_generator()
        # 
        usuario = User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password_1'],
            nombres=form.cleaned_data['nombres'],
            apellidos=form.cleaned_data['apellidos'],
            genero=form.cleaned_data['genero'],
            codregistro=code,
        )
        # enviar el código al email del usuario
        asunto = 'Confirmación email'
        mensaje = f'Código e verificación {code}'
        email_remitente = 'ise.david.casas@gmail.com'

        send_mail(asunto, mensaje, email_remitente, [form.cleaned_data['email'], ])
        # redirigir a la pantalla de validación
        
        return HttpResponseRedirect(reverse('user_app:user-verification'), kwargs={
            'pk': usuario.id
        })


# LOGIN
class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:panel')
    
    def form_valid(self, form):
        
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        
        login( self.request, user ) # peticion, usuario autenticado
        
        return super(LoginUser, self).form_valid(form)
    

# LOGOUT
class LogoutView(View):
    
    def get(self, request, *args, **kwargs):
        logout(request)
        
        return HttpResponseRedirect(
            reverse('users_app:user-login')
        )
        
# CHANGE PASSWORD
class UpdatePasswordView(FormView):
    template_name = 'users/update.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('users_app:user-login')
    
    def form_valid(self, form):
        
        # confirmamos que la clave actual es correcta
        usuario = self.request.user
        user_auth = authenticate(
            username=usuario.username,
            password=form.cleaned_data['password_1']
        )
        
        if user_auth:
            new_passw = form.cleaned_data['password_2']
            # configuramos la nueva contraseña con el hash
            usuario.set_password(new_passw)
            usuario.save()
            
            
        # por seguridad cerramos sesión
        logout( self.request )
        
        return super(UpdatePasswordView, self).form_valid(form)
        
# CONFIRMATION CODE
class CodeVerificationView(FormView):
    template_name = 'users/confirmation.html'
    form_class = VerificationForm
    success_url = reverse_lazy('users_app:user-login')
    
    def get_form_kwargs(self):
        kwargs = super(CodeVerificationView, self).get_form_kwargs()
        kwargs.update({ 'pk': self.kwargs['pk']})
        
        return kwargs
    
    def form_valid(self, form):
        
        User.objects.filter(
            id=self.kwargs['pk']
        ).update(is_active=True)
        
        return super(CodeVerificationView, self).form_valid(form)