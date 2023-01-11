from dataclasses import fields
from rest_framework import serializers
from medicamento.models import *

class MedicamentoFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicamentosFull
        fields = ('__all__')
        #read_only_fields = ('username_familiar',)