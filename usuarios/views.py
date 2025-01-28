from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('usuario_creado')  # Redirige a la página de éxito
    else:
        form = CustomUserCreationForm()
    return render(request, 'usuarios/register.html', {'form': form})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'usuarios/edit_profile.html', {'form': form})

def registro_requerido(request):
    return render(request, 'usuarios/registro_requerido.html')

def usuario_creado(request):
    return render(request, 'usuarios/usuario_creado.html')

