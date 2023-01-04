from django.contrib import admin

from app.models import *




#Vista de preregistro
class AdminPreRegistro(admin.ModelAdmin):
    list_display = ('nombre_paciente', 'apellido_paciente', 'rut_paciente','terminos_uso', 'timestamp')

class AdminEnfermera(admin.ModelAdmin):
    list_display = ('username_enfermera', 'rut_enfermera', 'direccion_enfermera','celular_enfermera', 'telefono_enfermera', 'telegram_enfermera')

class AdminNeurologo(admin.ModelAdmin):
    list_display = ('rut_neurologo', 'nombre_neurologo', 'apellido_neurologo', 'email_neurologo', 'telegram_neurologo')


class AdminDocumento(admin.ModelAdmin):
    list_display = ('titulo', 'documento', 'descripcion')



 


# Register your models here.

admin.site.register(Receta)
admin.site.register(Region)
admin.site.register(Provincia)
admin.site.register(Comuna)

admin.site.register(Medicamento)
admin.site.register(Neurologo, AdminNeurologo)


admin.site.register(Recordatorio_grabacion)
admin.site.register(Descuento)
admin.site.register(Descuento_usado)
admin.site.register(Familiar_paciente)
admin.site.register(Neurologo_paciente)
admin.site.register(Estado_monitoreo)
admin.site.register(Automonitoreo)

admin.site.register(Estado_animo)




admin.site.register(Enfermera, AdminEnfermera)
admin.site.register(Enfermera_paciente)
admin.site.register(Bitacora)
admin.site.register(Documento, AdminDocumento)
admin.site.register(Paciente_Documento)
admin.site.register(Preregistro, AdminPreRegistro)
admin.site.register(Enfermera_neurologo)
admin.site.register(RegistroCorreos)











