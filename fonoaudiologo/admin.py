from django.contrib import admin
from .models import Fonoaudiologo, Fonoaudiologo_paciente, Audio, Vocalizacion, Intensidad
# Register your models here.
admin.site.register(Fonoaudiologo)
admin.site.register(Fonoaudiologo_paciente)
admin.site.register(Audio)
admin.site.register(Vocalizacion)
admin.site.register(Intensidad)
