from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('registro-requerido/', views.registro_requerido, name='registro_requerido'),
    path('usuario-creado/', views.usuario_creado, name='usuario_creado'),  # Nueva ruta
]
