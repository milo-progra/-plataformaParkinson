from django import forms
from .models import *
from django import forms
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