from django.contrib import admin
from .models import Fonoaudiologo, Fonoaudiologo_paciente, Audio, Vocalizacion, Intensidad

class AdminFonoaudiologo(admin.ModelAdmin):
    list_display = ('rut_fonoaudiologo', 'nombre_fonoaudiologo', 'apellido_fonoaudiologo', 'direccion_fonoaudiologo', 'email_fonoaudiologo','telegram_fonoaudiologo')




# Register your models here.
admin.site.register(Fonoaudiologo, AdminFonoaudiologo)
admin.site.register(Fonoaudiologo_paciente)
admin.site.register(Audio)
admin.site.register(Vocalizacion)
admin.site.register(Intensidad)
