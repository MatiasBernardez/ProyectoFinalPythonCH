from django.db import models

# Create your models here.

class Psicologo(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    matricula = models.IntegerField()
    email = models.EmailField()
    telefono = models.IntegerField()
    zonaatencion = models.CharField(max_length=40)
    modalidadatencion = models.CharField(max_length=40)
    orientacion = models.CharField(max_length=40)
    especialidad = models.CharField(max_length=40)
    tipotratamiento = models.CharField(max_length=40)