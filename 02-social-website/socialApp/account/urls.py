from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import user_login, dashboard, register, edit



urlpatterns = [
    # path('login/', user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
    path('', include('django.contrib.auth.urls')),
    # path(
    #     'password-change/',
    #     auth_views.PasswordChangeView.as_view(),
    #     name='password_change'
    # ),
    # path(
    #     'password-change/done',
    #     auth_views.PasswordChangeDoneView.as_view(),
    #     name='password_change_done'
    # ),
    # path(
    #     'password_reset/',
    #     auth_views.PasswordResetView.as_view(),
    #     name='password_reset'
    # ),
    # path(
    #     'password_reset/done/',
    #     auth_views.PasswordResetDoneView.as_view(),
    #     name='password_reset_done'
    # ),
    # path(
    #     'reset/<uidb64>/<token>/',
    #     auth_views.PasswordResetConfirmView.as_view(),
    #     name='password_reset_confirm'
    # ),
    # path(
    #     'reset/done/',
    #     auth_views.PasswordResetCompleteView.as_view(),
    #     name='password_reset_complete'
    # ),
    path('dashboard/', dashboard, name='dashboard'),
]
