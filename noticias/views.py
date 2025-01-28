import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from .models import Noticia
from django.contrib.auth.decorators import login_required

def scrape_ign():
    url = "https://latam.ign.com/article/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    noticias = []
    for item in soup.select('article.article.NEWS')[:5]:  # Selecciona los artículos
        titulo = item.select_one('h3 a').get_text(strip=True)  # Encuentra el título dentro del enlace
        enlace = item.select_one('h3 a')['href']  # Obtiene el enlace del artículo
        noticias.append({
            'titulo': titulo,
            'enlace': enlace
        })

    return noticias

def scrape_gamespot():
    url = "https://www.gamespot.com/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    noticias = []
    for item in soup.select('div.content')[:5]:  # Selecciona las noticias
        titulo_element = item.select_one('summary.promo--metadata h2')  # Encuentra el título
        enlace_element = item.find_parent('a')  # Encuentra el enlace

        if titulo_element and enlace_element:  # Verifica que ambos elementos existan
            titulo = titulo_element.get_text(strip=True)
            enlace = enlace_element['href']
            noticias.append({
                'titulo': titulo,
                'enlace': enlace
            })

    return noticias

@login_required
def cargar_noticias(request):
    noticias_ign = scrape_ign()
    noticias_gamespot = scrape_gamespot()

    # Guardar noticias en la base de datos
    for noticia in noticias_ign + noticias_gamespot:
        Noticia.objects.get_or_create(titulo=noticia['titulo'], defaults={'contenido': noticia['enlace']})

    return render(request, 'noticias/lista_noticias.html', {'noticias': Noticia.objects.all()})
