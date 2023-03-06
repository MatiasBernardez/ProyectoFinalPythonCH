from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):

    return render (request, "AppBlog/inicio.html")

def especialidad(request):

    return render (request, "AppBlog/especialidad.html")

def modalidadatencion(request):

    return render (request, "AppBlog/modalidadatencion.html")

def orientacion(request):

    return render (request, "AppBlog/orientacion.html")

def tipotratamiento(request):

    return render (request, "AppBlog/tipotratamiento.html")

def zonaatencion(request):

    return render (request, "AppBlog/zonaatencion.html")