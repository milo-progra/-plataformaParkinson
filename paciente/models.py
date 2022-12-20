from django.db import models

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