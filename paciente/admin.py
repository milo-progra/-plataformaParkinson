from django.contrib import admin
from . models import Diabetes, Hipertension, Animo, Paciente, Familiar

#Vista de pacientes
class AdminPaciente(admin.ModelAdmin):
    list_display = ('nombre_paciente', 'rut_paciente', 'direccion_paciente', 'email_paciente', 'celular_paciente', 'telefono_paciente','telegram_paciente')

class AdminEnfermera(admin.ModelAdmin):
    list_display = ('username_enfermera', 'rut_enfermera', 'direccion_enfermera','celular_enfermera', 'telefono_enfermera', 'telegram_enfermera')


class AdminFamiliar(admin.ModelAdmin):
    list_display = ('nombre_familiar', 'rut_familiar', 'apellido_familiar', 'direccion_familiar', 'email_familiar', 'telefono_familiar', 'celular_familiar', 'telegram_familiar')



# Register your models here.
admin.site.register(Diabetes)
admin.site.register(Hipertension)
admin.site.register(Animo)
admin.site.register(Paciente, AdminPaciente)
admin.site.register(Familiar, AdminFamiliar)