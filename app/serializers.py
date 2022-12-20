from dataclasses import fields
from rest_framework import serializers
from .models import *

class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiar
        fields = ('__all__')
        read_only_fields = ('username_familiar',)

class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = ('__all__')
        read_only_fields = ('username_paciente',)


        
class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        #fields = ('__all__')
        read_only_fields=('url_archivo_audio',)
        fields = (["id","username_paciente", "timestamp", "url_archivo_audio", "jitter_ppq5_IA", "jitter_rap_IA", "maximum_pitch_IA", "error_jitter_ppq5_IA", "error_jitter_rap_IA", "error_maximum_pitch_IA" ])
        





