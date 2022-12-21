from django.contrib import admin

from app.models import *


#Vista de pacientes
class AdminPaciente(admin.ModelAdmin):
    list_display = ('nombre_paciente', 'id_paciente', 'rut_paciente', 'telegram_paciente')

# Register your models here.

admin.site.register(Receta)
admin.site.register(Region)
admin.site.register(Provincia)
admin.site.register(Comuna)
admin.site.register(Tipo_farmaco)
admin.site.register(Forma_farmaceutica)
admin.site.register(Dosis)
admin.site.register(Marca)
admin.site.register(Recomendacion_consumo)
admin.site.register(Laboratorio)
admin.site.register(Via_ingesta)
admin.site.register(Medicamento)
admin.site.register(Neurologo)
admin.site.register(Paciente, AdminPaciente)
admin.site.register(Familiar)
admin.site.register(Recordatorio_grabacion)
admin.site.register(Descuento)
admin.site.register(Descuento_usado)
admin.site.register(Familiar_paciente)
admin.site.register(Neurologo_paciente)
admin.site.register(Estado_monitoreo)
admin.site.register(Automonitoreo)

admin.site.register(Estado_animo)
admin.site.register(Fonoaudiologo_paciente)
admin.site.register(Fonoaudiologo)
admin.site.register(Audio)
admin.site.register(Vocalizacion)
admin.site.register(Intensidad)
admin.site.register(Enfermera)
admin.site.register(Enfermera_paciente)
admin.site.register(Bitacora)
admin.site.register(Documento)
admin.site.register(Paciente_Documento)
admin.site.register(Preregistro)
admin.site.register(Enfermera_neurologo)
admin.site.register(RegistroCorreos)











