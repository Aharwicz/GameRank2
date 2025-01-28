from django.db import models
from usuarios.models import CustomUser

class Developer(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Publisher(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Juego(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    lanzamiento = models.DateField()
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    puntaje_metacritic = models.IntegerField()

    def __str__(self):
        return self.titulo

class Ranking(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()

    class Meta:
        unique_together = ('usuario', 'juego')

    def __str__(self):
        return f'{self.usuario.username} - {self.juego.titulo}: {self.puntuacion}'

