from django import forms
from .models import *
from django import forms

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


