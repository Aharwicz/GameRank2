from django.conf import settings
from django.shortcuts import render
from juegos.models import Publisher, Developer, Juego
from django.db.models import Avg

def inicio(request):
    # Obtener rankings ordenados de mayor a menor según el promedio de puntajes
    ranking_publishers = Publisher.objects.annotate(promedio=Avg('rankingpublisher__puntuacion')).order_by('-promedio')[:5]
    ranking_developers = Developer.objects.annotate(promedio=Avg('rankingdeveloper__puntuacion')).order_by('-promedio')[:5]
    ranking_juegos = Juego.objects.annotate(promedio=Avg('ranking__puntuacion')).order_by('-promedio')[:5]

    contexto = {
        'imagen_destacada': "/media/Destacados/Spec-Ops-The-Line-Main.jpg",
        'ranking_publishers': ranking_publishers,
        'ranking_developers': ranking_developers,
        'ranking_juegos': ranking_juegos,
    }
    return render(request, 'explicacion/inicio.html', contexto)

def acerca_de(request):
    return render(request, 'explicacion/acerca_de.html')
