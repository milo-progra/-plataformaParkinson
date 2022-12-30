from django import forms
from .models import *
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from app.models import Preregistro, Estado_animo


class FormPreregistro(forms.ModelForm):
    class Meta:
        model = Preregistro
        fields ='__all__'

        widgets={
            'nombre_paciente': forms.TextInput(attrs={
                'class': 'form-control mb-2',
            'placeholder': 'Ingrese su Nombre'
        }),

        'apellido_paciente': forms.TextInput(attrs={
                'class': 'form-control mb-2',
            'placeholder': 'Ingrese su Apellido'
        }),
        'rut_paciente': forms.TextInput(attrs={
                'class': 'form-control mb-2',
            'placeholder': 'Ejemplo: 12345678-2'
        }),
        'telefono_paciente': forms.TextInput(attrs={
                'class': 'form-control mb-2',
            'placeholder': 'Ejemplo: 912345678'
        }),
        'email_paciente': forms.EmailInput(attrs={
                'class': 'form-control mb-2',
            'placeholder': 'correo@correo.com'
        }),
        }



class FormEmociones(forms.ModelForm):
    class Meta:
        model = Estado_animo

        fields =[
            'animo',

        ]
        labels={
            'animo':'Animo',

        }

        widgets={
            'animo': forms.RadioSelect(),
        }        


class AdminFormaCreacionUsuario(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")

        return password2

    def save(self, commit=True):
        usuario = super(AdminFormaCreacionUsuario, self).save(commit=False)
        usuario.set_password(self.cleaned_data["password1"])
        if commit:
            usuario.save()
        return usuario



class AdminFormaActualizar(forms.ModelForm):
    # variable para que el admin solo pueda ver la contraseña
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password', 'password')

    def clean_password(self):
        return self.initial['password']