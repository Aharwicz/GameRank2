from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class CustomUserChangeForm(forms.ModelForm):  # Quitamos UserChangeForm para excluir la contraseña
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'foto_perfil']  # Excluimos el campo password
