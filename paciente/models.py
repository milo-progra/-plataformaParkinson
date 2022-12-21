from django.db import models
from usuario.models import Usuario 
# Create your models here.
# Modelo para Diabetes
class Diabetes(models.Model):
    id_diabetes     = models.AutoField('Id Diabetes', primary_key=True)
    tipo_diabetes = models.CharField('Tipo Diabetes', max_length=100)

    def __str__(self):
        return self.tipo_diabetes 



# Modelo para Hipertension
class Hipertension(models.Model):
    id_hipertension     = models.AutoField('Id Hipertension', primary_key=True)
    estado_hipertension = models.CharField('Estado Hipertension', max_length=100)

    def __str__(self):
        return self.estado_hipertension         


# Modelo para Animo
class Animo(models.Model):
    id_Animo = models.AutoField('Id Animo', primary_key=True)
    valor_animo = models.IntegerField('Valor Animo')
    nombre_animo    = models.CharField('Nombre Animo', max_length=50, null=True, blank=True)
    #codigo_emoticon = models.CharField('Codigo Emoticon', max_length=50, null=True, blank=True)
    def __str__(self):
        return self.nombre_animo


