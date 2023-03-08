from django import forms


class PsicologoFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    matricula = forms.IntegerField()
    email = forms.EmailField()
    telefono = forms.IntegerField()
    zonaatencion = forms.CharField(max_length=40)
    modalidadatencion = forms.CharField(max_length=40)
    orientacion = forms.CharField(max_length=40)
    especialidad = forms.CharField(max_length=40)
    tipotratamiento = forms.CharField(max_length=40)