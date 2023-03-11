from django.shortcuts import render
from django.http import HttpResponse
from .models import Psicologo
from .forms import PsicologoFormulario
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def inicio(request):

    return render (request, "AppBlog/inicio.html")

@login_required
def especialidad(request):

    return render (request, "AppBlog/especialidad.html")

@login_required
def modalidadatencion(request):

    return render (request, "AppBlog/modalidadatencion.html")

@login_required
def orientacion(request):

    return render (request, "AppBlog/orientacion.html")

@login_required
def tipotratamiento(request):

    return render (request, "AppBlog/tipotratamiento.html")

@login_required
def zonaatencion(request):

    return render (request, "AppBlog/zonaatencion.html")

@login_required
def inicio(request):

    if request.method == 'POST':

        miFormulario = PsicologoFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            psicologo = Psicologo(nombre=informacion['nombre'],
            apellido=informacion['apellido'], matricula=informacion['matrícula'],
            email=informacion['email'], telefono=informacion['teléfono'],
            zonaatencion=informacion['zona_de_atención'], modalidadatencion=informacion['modalidad_de_atención'],
            orientacion=informacion['orientación'], especialidad=informacion['especialidad'],
            tipotratamiento=informacion['tipo_de_tratamiento'])

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

def leerPsicologos(request):

    psicologos = Psicologo.objects.all()

    contexto = {"psicologos":psicologos}

    return render(request, "AppBlog/leerPsicologos.html", contexto)

def eliminarPsicologo(request, psicologo_nombre):

    psicologo = Psicologo.objects.get(nombre=psicologo_nombre)
    psicologo.delete()

    psicologos = Psicologo.objects.all()

    contexto = {"psicologos":psicologos}

    return render(request, "AppBlog/leerPsicologos.html", contexto)

def editarPsicologo(request, psicologo_nombre):

    psicologo = Psicologo.objects.get(nombre=psicologo_nombre)

    if request.method == 'POST':

        miFormulario = PsicologoFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            psicologo.nombre = informacion['nombre']
            psicologo.apellido = informacion['apellido']
            psicologo.matricula = informacion['matricula']
            psicologo.email = informacion['email']
            psicologo.telefono = informacion['telefono']
            psicologo.zonaatencion = informacion['zonaatencion']
            psicologo.modalidadatencion = informacion['modalidadatencion']
            psicologo.orientacion = informacion['orientacion']
            psicologo.especialidad = informacion['especialidad']
            psicologo.tipotratamiento = informacion['tipotratamiento']

            psicologo.save()

            return render(request, "AppBlog/inicio.html")

    else:

        miFormulario = PsicologoFormulario(initial={'nombre': psicologo.nombre, 'apellido': psicologo.apellido,
        'matricula': psicologo.matricula, 'email': psicologo.email, 'telefono': psicologo.telefono,
        'zonaatencion': psicologo.zonaatencion, 'modalidadatencion': psicologo.modalidadatencion,
        'orientacion': psicologo.orientacion, 'especialidad': psicologo.especialidad,
        'tipotratamiento': psicologo.tipotratamiento})

    return render(request, "AppBlog/editarPsicologo.html", {"miFormulario":miFormulario, "psicologo_nombre":psicologo_nombre })

class PsicologoList(ListView):

    model = Psicologo
    template_name = "AppBlog/psicologo_list.html"

class PsicologoDetalle(DetailView):

    model = Psicologo
    template_name = "AppBlog/psicologo_detalle.html"

class PsicologoCreacion(CreateView):

    model = Psicologo
    success_url = "/AppBlog/psicologo/list"
    fields = ['nombre', 'apellido', 'matricula', 'email', 'telefono', 'zonaatencion', 'modalidadatencion', 'orientacion', 'especialidad', 'tipotratamiento']

class PsicologoUpdate(UpdateView):

    model = Psicologo
    success_url = "/AppBlog/psicologo/list"
    fields = ['nombre', 'apellido', 'matricula', 'email', 'telefono', 'zonaatencion', 'modalidadatencion', 'orientacion', 'especialidad', 'tipotratamiento']

class PsicologoDelete(DeleteView):

    model = Psicologo
    success_url = "/AppBlog/psicologo/list"

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contraseña)


            if user is not None:
                login(request, user)

                return render(request, "AppBlog/inicio.html", {"mensaje":f"Bienvenido {usuario}"})

            else:

                return render(request, "AppBlog/inicio.html", {"mensaje":"Error, datos incorrectos"})

    else:

                return render(request, "AppBlog/inicio.html", {"mensaje":"Error, formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppBlog/login.html", {'form':form})

def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request,"AppBlog/inicio.html", {"mensaje":"Usuario creado :)"})


    else:
        form = UserRegisterForm()


    return render(request,"AppBlog/registro.html", {"form":form})