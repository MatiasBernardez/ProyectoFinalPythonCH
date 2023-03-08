from django.shortcuts import render
from django.http import HttpResponse
from .models import Psicologo
from .forms import PsicologoFormulario

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


def inicio(request):

    if request.method == 'POST':

        miFormulario = PsicologoFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            psicologo = Psicologo(nombre=informacion['nombre'],
            apellido=informacion['apellido'], matricula=informacion['matricula'],
            email=informacion['email'], telefono=informacion['telefono'],
            zonaatencion=informacion['zonaatencion'], modalidadatencion=informacion['modalidadatencion'],
            orientacion=informacion['orientacion'], especialidad=informacion['especialidad'],
            tipotratamiento=informacion['tipotratamiento'])

            psicologo.save()

            return render (request, "AppBlog/inicio.html")

    else:

        miFormulario = PsicologoFormulario()

    return render(request, "AppBlog/inicio.html", {"miFormulario":miFormulario})

def buscarzonaatencion(request):

    if request.GET["zonaatencion"]:

        zonaatencion = request.GET['zonaatencion']
        psicologo = Psicologo.objects.filter(zonaatencion__icontains=zonaatencion)

        return render(request, "AppBlog/zonaatencion.html", {"psicologo":psicologo, "zonaatencion":zonaatencion})

    else:

        respuesta = "No hay datos con esa descripción."

    return render(request, "AppBlog/zonaatencion.html", {"respuesta":respuesta})

def buscarmodalidadatencion(request):

    if request.GET["modalidadatencion"]:

        modalidadatencion = request.GET['modalidadatencion']
        psicologo = Psicologo.objects.filter(modalidadatencion__icontains=modalidadatencion)

        return render(request, "AppBlog/modalidadatencion.html", {"psicologo":psicologo, "modalidadatencion":modalidadatencion})

    else:

        respuesta = "No hay datos con esa descripción."

    return render(request, "AppBlog/modalidadatencion.html", {"respuesta":respuesta})

def buscartipotratamiento(request):

    if request.GET["tipotratamiento"]:

        tipotratamiento = request.GET['tipotratamiento']
        psicologo = Psicologo.objects.filter(tipotratamiento__icontains=tipotratamiento)

        return render(request, "AppBlog/tipotratamiento.html", {"psicologo":psicologo, "tipotratamiento":tipotratamiento})

    else:

        respuesta = "No hay datos con esa descripción."

    return render(request, "AppBlog/tipotratamiento.html", {"respuesta":respuesta})

def buscarorientacion(request):

    if request.GET["orientacion"]:

        orientacion = request.GET['orientacion']
        psicologo = Psicologo.objects.filter(orientacion__icontains=orientacion)

        return render(request, "AppBlog/orientacion.html", {"psicologo":psicologo, "orientacion":orientacion})

    else:

        respuesta = "No hay datos con esa descripción."

    return render(request, "AppBlog/orientacion.html", {"respuesta":respuesta})

def buscarespecialidad(request):

    if request.GET["especialidad"]:

        especialidad = request.GET['especialidad']
        psicologo = Psicologo.objects.filter(especialidad__icontains=especialidad)

        return render(request, "AppBlog/especialidad.html", {"psicologo":psicologo, "especialidad":especialidad})

    else:

        respuesta = "No hay datos con esa descripción."

    return render(request, "AppBlog/especialidad.html", {"respuesta":respuesta})