from django.contrib import admin
from .models import *



class AdminMedicamento(admin.ModelAdmin):
    list_display = ('sucursal', 'id_medicamento', 'nombre_medicamento', 'medida_medicamento' ,'cantidad_comprimidos','stockSistema', 'stockDiario', 'timestamp', 'fecha_actu_stock')


# Register your models here.
admin.site.register(Tipo_farmaco)
admin.site.register(Forma_farmaceutica)
admin.site.register(Dosis)
admin.site.register(Marca)
admin.site.register(Recomendacion_consumo)
admin.site.register(Laboratorio)
admin.site.register(Via_ingesta)
admin.site.register(MedicamentosFull, AdminMedicamento)