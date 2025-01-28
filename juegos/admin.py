from django.contrib import admin
from .models import Developer, Publisher, Juego

@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'especialidad']

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'pais']

@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'genero', 'lanzamiento', 'developer', 'publisher', 'puntaje_metacritic']
