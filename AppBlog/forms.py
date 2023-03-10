from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


class PsicologoFormulario(LoginRequiredMixin, forms.Form):

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


class UserRegisterForm(UserCreationForm):

    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Modificar email")
    password1 = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la nueva contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}