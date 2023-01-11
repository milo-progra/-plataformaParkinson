from dataclasses import fields
from rest_framework import serializers
from medicamento.models import *

class MedicamentoFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicamentosFull
        fields = ('__all__')    
        read_only_fields = ('id_medicamento', 'sucursal', 'sku', 'laboratorio', 'marca', 'nombre_medicamento', 'medida_medicamento', 'cantidad_comprimidos', 'tipo_farmaco', 'recomendacion', 'via_ingesta', 'forma_farmaceutica', 'stockSistema', 'timestamp')