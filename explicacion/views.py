from django.shortcuts import render

def inicio(request):
    return render(request, 'explicacion/inicio.html')

def acerca_de(request):
    return render(request, 'explicacion/acerca_de.html')
