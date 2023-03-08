from django import forms


class PsicologoFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    matrícula = forms.IntegerField()
    email = forms.EmailField()
    teléfono = forms.IntegerField()
    zona_de_atención = forms.CharField(max_length=40)
    modalidad_de_atención = forms.CharField(max_length=40)
    orientación = forms.CharField(max_length=40)
    especialidad = forms.CharField(max_length=40)
    tipo_de_tratamiento = forms.CharField(max_length=40)