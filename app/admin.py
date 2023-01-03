from django.contrib import admin

from app.models import *


#Vista de pacientes
class AdminPaciente(admin.ModelAdmin):
    list_display = ('nombre_paciente', 'id_paciente', 'rut_paciente', 'telegram_paciente')

#Vista de pacientes
class AdminPreRegistro(admin.ModelAdmin):
    list_display = ('nombre_paciente', 'apellido_paciente', 'rut_paciente','terminos_uso', 'timestamp')


# Register your models here.

admin.site.register(Receta)
admin.site.register(Region)
admin.site.register(Provincia)
admin.site.register(Comuna)

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




admin.site.register(Enfermera)
admin.site.register(Enfermera_paciente)
admin.site.register(Bitacora)
admin.site.register(Documento)
admin.site.register(Paciente_Documento)
admin.site.register(Preregistro, AdminPreRegistro)
admin.site.register(Enfermera_neurologo)
admin.site.register(RegistroCorreos)











