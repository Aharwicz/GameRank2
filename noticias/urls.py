from django.urls import path
from .views import cargar_noticias

urlpatterns = [
    path('noticias/', cargar_noticias, name='lista_noticias'),
]
