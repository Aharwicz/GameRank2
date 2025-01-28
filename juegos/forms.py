from django import forms
from .models import Developer, Publisher, Juego

class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ['nombre', 'especialidad']  # Campos específicos del modelo Developer

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['nombre', 'pais']  # Campos específicos del modelo Publisher

class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = ['titulo', 'genero', 'lanzamiento', 'developer', 'publisher', 'puntaje_metacritic']
        # Solo los campos que deben ser editables por el usuario
