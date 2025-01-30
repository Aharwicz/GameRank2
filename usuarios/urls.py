from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('registro-requerido/', views.registro_requerido, name='registro_requerido'),
    path('usuario-creado/', views.usuario_creado, name='usuario_creado'),
    
    # Rutas para cambio de contraseña
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='usuarios/password_change.html'), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='usuarios/password_change_done.html'), name='password_change_done'),
]
