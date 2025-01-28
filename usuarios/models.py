from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    foto_perfil = models.ImageField(
        upload_to='fotos_perfil/',
        blank=True,
        null=True,
        default='fotos_perfil/default_profile.jpg'  # Ruta de la imagen predeterminada
    )
