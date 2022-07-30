from django.shortcuts import render
from django.views.generic import (
    TemplateView
)


class LoginUser(TemplateView):
    template_name = "users/login.html"
