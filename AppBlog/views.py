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


def psicologoFormulario(request):

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

    return render(request, "AppBlog/psicologoFormulario.html", {"miFormulario":miFormulario})

def busquedaNombrePsicologo(request):

    return render(request, "AppBlog/busquedaNombrePsicologo.html")

def buscar(request):

    if request.GET["nombre"]:

        nombre = request.GET['nombre']
        psicologo = Psicologo.objects.filter(nombre__icontains=nombre)

        return render(request, "AppBlog/resultadosBusqueda.html", {"psicologo":psicologo, "nombre":nombre})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)