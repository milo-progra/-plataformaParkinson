from django import forms
from .models import *
from django import forms

class UsuarioForm(forms.ModelForm):

    username = forms.CharField(label='Nombre de Usuario', widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Ingrese su nombre de usuario',
            'id': 'username'
        }))

    first_name = forms.CharField(label=' Ingrese su Nombre', widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Ingrese su Nombre',
            'id': 'first_name'
        }))

    last_name = forms.CharField(label=' Ingrese su Apellido', widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Ingrese su Apellido',
            'id': 'last_name'
        }))

    email = forms.EmailField(label='Correo Electronico', widget=forms.EmailInput(attrs={
        'class': 'form-control mb-2',
        'placeholder': 'Ingrese su correo electronico',
        'id': 'email'
    }))

    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Ingrese Contraseña',
            'id': 'password'
        }))

    class Meta:
        model = Usuario
        fields = 'username', 'first_name', 'last_name', 'email', 'password', 'tipo_usuario'

    def clean_password(self):
        """ validacion de contraseña

        metodo que valida la contraseña 
        """
        password = self.cleaned_data.get('password')
        return password

    def save(self, commit=True):
        # guardar la informacion del registro en la variable user
        user = super().save(commit=False)
        # encriptar contraseña
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

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

class FormAutomonitoreo(forms.ModelForm):
    class Meta:
        model = Automonitoreo

        fields =[
            'estado_monitoreo',

        ]
        labels={
            'estado_monitoreo':'Estado Monitoreo',

        }

        widgets={
            'estado_monitoreo': forms.RadioSelect(),
        }

class FormTelegram(forms.ModelForm):
    class Meta:
        model = Paciente

        fields =[
            'telegram_paciente',

        ]
        labels={
            'telegram_paciente':'Telegram Paciente',

        }

        widgets={
            'telegram_paciente': forms.TextInput(attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Ingrese su Telegram',
            'id': 'id_telegram'
        }),
        }

class FormComentario(forms.ModelForm):
    class Meta:
        model = Vocalizacion

        fields =[
            'comentario',

        ]
        labels={
            'comentario':'Comentario Vocalización',

        }

        widgets={
            'comentario': forms.Textarea(attrs={
            'rows': '5',
            'placeholder': 'Ingrese su Comentario'
        }),
        }

class FormComentarioIntensidad(forms.ModelForm):
    class Meta:
        model = Intensidad

        fields =[
            'comentario',

        ]
        labels={
            'comentario':'Comentario Intensidad',

        }

        widgets={
            'comentario': forms.Textarea(attrs={
            'rows': '5',
            'placeholder': 'Ingrese su Comentario'
        }),
        }

class FormBitacora(forms.ModelForm):
    class Meta:
        model = Bitacora

        fields =[
            # 'username_paciente',
            'anotaciones',

        ]
        labels={
            # 'username_paciente':'Paciente',
            'anotaciones':'Anotaciones',

        }

        widgets={
            'anotaciones': forms.Textarea(attrs={
            'rows': '5',
            'placeholder': 'Ingrese su anotaciones'
        }),
        }

class FormReceta(forms.ModelForm):
    class Meta:
        model = Receta

        fields =[
            # 'username_paciente',
            'horario_medicamento',
            'medicamento',
            'dosis',

        ]

        labels={
            # 'username_paciente':'Paciente',
            'horario_medicamento' : "Horario Medicamento",
            'medicamento': "Medicamento",
            'dosis' :"Dosis",

        }

        widgets={
            'horario_medicamento': forms.TextInput(attrs={
            'placeholder': '00:00:00'
        }),
        }

class FormMedicamento(forms.ModelForm):
    class Meta:
        model = Medicamento

        fields =[
            # 'username_paciente',
            'laboratorio',
            'marca',
            'nombre_medicamento',
            'medida_medicamento',
            'cantidad_comprimidos',
            'tipo_farmaco',
            'forma_farmaceutica',
            'recomendacion',
            'via_ingesta',
            
        ]

        labels={
            # 'username_paciente':'Paciente',
            'horario_medicamento' : "Horario Medicamento",
            'medicamento': "Medicamento",
            'dosis' :"Dosis",


            'nombre_medicamento': "Nombre Medicamento",
            'medida_medicamento': "Medida Medicamento",
            'cantidad_comprimidos':"Cantidad Comprimidos",
            'tipo_farmaco':"Tipo Farmaco",
            'forma_farmaceutica':"Forma Farmaceutica",
            'recomendacion':"Recomendacion",
            'marca':"Marca",
            'via_ingesta':"Via Ingesta",
            'laboratorio':"Laboratorio",
        }

class FormDocumentos(forms.ModelForm):

    class Meta:
        model = Paciente_Documento
        fields =[
            'documento',
            # 'autorizado',
        ]
        labels={
            'documento' : "Seleccione Documento para Autorizar",
            # 'autorizado': "Autorizado",
        }
        widgets={
            'documento': forms.RadioSelect(),
        }

class FormDocumentoAdmin(forms.ModelForm):
    class Meta:
        model = Documento
        fields ='__all__'

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

class PreregistroUsuarioForm(forms.ModelForm):

    username = forms.CharField(label='Nombre de Usuario', widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Ingrese su nombre de usuario',
            'id': 'username'
        }))

    first_name = forms.CharField(label=' Ingrese su Nombre', widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Ingrese su Nombre',
            'id': 'first_name'
        }))

    last_name = forms.CharField(label=' Ingrese su Apellido', widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Ingrese su Apellido',
            'id': 'last_name'
        }))

    email = forms.EmailField(label='Correo Electronico', widget=forms.EmailInput(attrs={
        'class': 'form-control mb-2',
        'placeholder': 'Ingrese su correo electronico',
        'id': 'email'
    }))

    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Ingrese Contraseña',
            'id': 'password'
        }))

    class Meta:
        model = Usuario
        fields = 'username', 'first_name', 'last_name', 'email', 'password'

    def clean_password(self):
        """ validacion de contraseña

        metodo que valida la contraseña 
        """
        password = self.cleaned_data.get('password')
        return password

    def save(self, commit=True):
        # guardar la informacion del registro en la variable user
        user = super().save(commit=False)
        # encriptar contraseña
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
        
class FormRegPaciente(forms.ModelForm):
    class Meta:
        model = Paciente

        fields ='__all__'
        
class FormEnfPac(forms.ModelForm):
    class Meta:
        model = Enfermera_paciente

        fields =[           
            'username_paciente'
        ]

        labels={
           
            'username_paciente' : "Seleccione Paciente para Vincular con Enfermera",
        }

class FormNeuPac(forms.ModelForm):
    class Meta:
        model = Neurologo_paciente

        fields =[           
            'username_paciente'
        ]

        labels={
           
            'username_paciente' : "Seleccione Paciente para Vincular con Neurologo",
        }

class AudioForm(forms.ModelForm): 
    """Form definition for Audio.""" 
 
    class Meta: 
        model = Audio 
        fields = ('jitter_ppq5', 'jitter_rap', 'maximum_pitch', 'error_jitter_ppq5', 'error_jitter_rap', 'error_maximum_pitch')

        
