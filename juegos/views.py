from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Avg
from .models import Developer, Publisher, Juego, RankingDeveloper, RankingPublisher, Ranking
from .forms import DeveloperForm, PublisherForm, JuegoForm

# Verifica si el usuario es administrador
def is_admin(user):
    return user.is_staff

# **Listas accesibles para usuarios registrados**
@login_required(login_url='registro_requerido')
def juego_list(request):
    juegos = Juego.objects.annotate(promedio_usuarios=Avg('ranking__puntuacion'))
    user_rankings = {
        ranking.juego.id: ranking.puntuacion
        for ranking in Ranking.objects.filter(usuario=request.user)
    }
    for juego in juegos:
        juego.user_score = user_rankings.get(juego.id, None)

    return render(request, 'juegos/juego_list.html', {
        'juegos': juegos,
        'user_rankings': user_rankings,
    })

@login_required(login_url='registro_requerido')
def developer_list(request):
    developers = Developer.objects.annotate(promedio_usuarios=Avg('rankingdeveloper__puntuacion'))
    user_rankings = {
        ranking.developer.id: ranking.puntuacion
        for ranking in RankingDeveloper.objects.filter(usuario=request.user)
    }
    for developer in developers:
        developer.user_score = user_rankings.get(developer.id, None)

    return render(request, 'juegos/developer_list.html', {
        'developers': developers,
        'user_rankings': user_rankings,
    })

@login_required(login_url='registro_requerido')
def publisher_list(request):
    publishers = Publisher.objects.annotate(promedio_usuarios=Avg('rankingpublisher__puntuacion'))
    user_rankings = {
        ranking.publisher.id: ranking.puntuacion
        for ranking in RankingPublisher.objects.filter(usuario=request.user)
    }
    for publisher in publishers:
        publisher.user_score = user_rankings.get(publisher.id, None)

    return render(request, 'juegos/publisher_list.html', {
        'publishers': publishers,
        'user_rankings': user_rankings,
    })

# **Puntuar o editar puntaje de una entidad**
@login_required(login_url='registro_requerido')
def rank_juego(request, pk):
    juego = get_object_or_404(Juego, pk=pk)
    if request.method == 'POST':
        puntuacion = request.POST.get('puntuacion')
        if puntuacion:
            Ranking.objects.update_or_create(
                usuario=request.user,
                juego=juego,
                defaults={'puntuacion': puntuacion}
            )
    return redirect('juego_list')

@login_required(login_url='registro_requerido')
def rank_developer(request, pk):
    developer = get_object_or_404(Developer, pk=pk)
    if request.method == 'POST':
        puntuacion = request.POST.get('puntuacion')
        if puntuacion:
            RankingDeveloper.objects.update_or_create(
                usuario=request.user,
                developer=developer,
                defaults={'puntuacion': puntuacion}
            )
    return redirect('developer_list')

@login_required(login_url='registro_requerido')
def rank_publisher(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        puntuacion = request.POST.get('puntuacion')
        if puntuacion:
            RankingPublisher.objects.update_or_create(
                usuario=request.user,
                publisher=publisher,
                defaults={'puntuacion': puntuacion}
            )
    return redirect('publisher_list')

# **CRUD exclusivo para administradores (Juegos)**
@user_passes_test(is_admin, login_url='registro_requerido')
def juego_add(request):
    if request.method == 'POST':
        form = JuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('juego_list')
    else:
        form = JuegoForm()
    return render(request, 'juegos/juego_form.html', {'form': form})

@user_passes_test(is_admin, login_url='registro_requerido')
def juego_edit(request, pk):
    juego = get_object_or_404(Juego, pk=pk)
    if request.method == 'POST':
        form = JuegoForm(request.POST, instance=juego)
        if form.is_valid():
            form.save()
            return redirect('juego_list')
    else:
        form = JuegoForm(instance=juego)
    return render(request, 'juegos/juego_form.html', {'form': form})

@user_passes_test(is_admin, login_url='registro_requerido')
def juego_delete(request, pk):
    juego = get_object_or_404(Juego, pk=pk)
    if request.method == 'POST':
        juego.delete()
        return redirect('juego_list')
    return render(request, 'juegos/juego_confirm_delete.html', {'juego': juego})

# **CRUD exclusivo para administradores (Developers)**
@user_passes_test(is_admin, login_url='registro_requerido')
def developer_add(request):
    if request.method == 'POST':
        form = DeveloperForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('developer_list')
    else:
        form = DeveloperForm()
    return render(request, 'juegos/developer_form.html', {'form': form})

@user_passes_test(is_admin, login_url='registro_requerido')
def developer_edit(request, pk):
    developer = get_object_or_404(Developer, pk=pk)
    if request.method == 'POST':
        form = DeveloperForm(request.POST, instance=developer)
        if form.is_valid():
            form.save()
            return redirect('developer_list')
    else:
        form = DeveloperForm(instance=developer)
    return render(request, 'juegos/developer_form.html', {'form': form})

@user_passes_test(is_admin, login_url='registro_requerido')
def developer_delete(request, pk):
    developer = get_object_or_404(Developer, pk=pk)
    if request.method == 'POST':
        developer.delete()
        return redirect('developer_list')
    return render(request, 'juegos/developer_confirm_delete.html', {'developer': developer})

# **CRUD exclusivo para administradores (Publishers)**
@user_passes_test(is_admin, login_url='registro_requerido')
def publisher_add(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publisher_list')
    else:
        form = PublisherForm()
    return render(request, 'juegos/publisher_form.html', {'form': form})

@user_passes_test(is_admin, login_url='registro_requerido')
def publisher_edit(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return redirect('publisher_list')
    else:
        form = PublisherForm(instance=publisher)
    return render(request, 'juegos/publisher_form.html', {'form': form})

@user_passes_test(is_admin, login_url='registro_requerido')
def publisher_delete(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        publisher.delete()
        return redirect('publisher_list')
    return render(request, 'juegos/publisher_confirm_delete.html', {'publisher': publisher})
