from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Avg
from .models import Developer, Publisher, Juego, Ranking
from .forms import DeveloperForm, PublisherForm, JuegoForm

# Verifica si el usuario es administrador
def is_admin(user):
    return user.is_staff

# **Listas accesibles para usuarios registrados**
@login_required(login_url='registro_requerido')
def developer_list(request):
    developers = Developer.objects.all()
    return render(request, 'juegos/developer_list.html', {'developers': developers})

@login_required(login_url='registro_requerido')
def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'juegos/publisher_list.html', {'publishers': publishers})

@login_required(login_url='registro_requerido')
def juego_list(request):
    # Calcula el promedio de los puntajes para cada juego
    juegos = Juego.objects.annotate(promedio_usuarios=Avg('ranking__puntuacion'))
    # Obtener el puntaje actual del usuario para cada juego y añadirlo al objeto
    for juego in juegos:
        ranking_usuario = Ranking.objects.filter(usuario=request.user, juego=juego).first()
        juego.user_score = ranking_usuario.puntuacion if ranking_usuario else None

    return render(request, 'juegos/juego_list.html', {
        'juegos': juegos,
    })

# **Vista para puntuar juegos**
@login_required(login_url='registro_requerido')
def rank_juego(request, pk):
    juego = get_object_or_404(Juego, pk=pk)
    if request.method == 'POST':
        puntuacion = request.POST.get('puntuacion')
        if puntuacion:
            try:
                puntuacion = int(puntuacion)
                if puntuacion < 1 or puntuacion > 100:
                    raise ValueError("Puntuación fuera de rango")
            except ValueError:
                return redirect('juego_list')

            # Crear o actualizar el ranking del usuario para el juego
            Ranking.objects.update_or_create(
                usuario=request.user,
                juego=juego,
                defaults={'puntuacion': puntuacion}
            )

            # Si fue creado o actualizado correctamente, redirigir
            return redirect('juego_list')

    # Si no es un POST, redirigir al listado de juegos
    return redirect('juego_list')

# **CRUD exclusivo para administradores**
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
