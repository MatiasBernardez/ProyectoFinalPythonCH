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

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Matrícula: {self.matricula} - Email: {self.email} - Teléfono: {self.telefono} - Zona de atención: {self.zonaatencion} - Modalidad de atención: {self.modalidadatencion} - Orientación: {self.orientacion} - Especialidad: {self.especialidad} - Tipo de tratamiento: {self.tipotratamiento}"