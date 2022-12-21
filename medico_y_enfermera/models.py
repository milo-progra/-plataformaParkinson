from django.db import models
from django.db import models
# Create your models here.

# Modelo para Institucion
class Institucion(models.Model): 
    nombre_institucion = models.CharField('Nombre Institución', max_length=100)
    comuna = models.ForeignKey(to='app.comuna', on_delete=models.CASCADE, verbose_name="Comuna", null=True)
    descripcion = models.CharField('Descripción Institución',max_length=2000)
 
    def __str__(self): 
        return self.nombre_institucion 
