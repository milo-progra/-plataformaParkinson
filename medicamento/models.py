from django.db import models

# Create your models here.

# Modelo para Tipo_farmaco
class Tipo_farmaco(models.Model):
    id_tipo_farmaco     = models.AutoField('Id Tipo Farmaco', primary_key=True)
    tipo_farmaco = models.CharField('Tipo Farmaco', max_length=100)
    descripcion_tipo_farmaco = models.CharField('Descripcion Tipo Farmaco', max_length=400)

    def __str__(self):
        return self.tipo_farmaco

# Modelo para Forma_farmaceutica
class Forma_farmaceutica(models.Model):
    id_forma_farmaceutica    = models.AutoField('Id Forma Farmaceutica', primary_key=True)
    forma_farmaceutica = models.CharField('Forma Farmaceutica', max_length=100)

    def __str__(self):
        return self.forma_farmaceutica 

# Modelo para Dosis
class Dosis(models.Model):
    id_dosis     = models.AutoField('Id Dosis', primary_key=True)
    cantidad_dosis = models.DecimalField('Cantidad Dosis', max_digits=3, decimal_places=2)
    descripcion = models.CharField('Descripcion', max_length=5)


    def __str__(self):
        return str(self.cantidad_dosis)+' - '+ str(self.descripcion)

# Modelo para Marca
class Marca(models.Model):
    id_marca     = models.AutoField('Id Marca', primary_key=True)
    marca = models.CharField('Marca', max_length=100)

    def __str__(self):
        return self.marca


# Modelo para Recomendacion_consumo
class Recomendacion_consumo(models.Model):
    id_recomendacion = models.AutoField('Id Recomendacion', primary_key=True)
    recomendacion = models.CharField('Recomendacion', max_length=100)

    def __str__(self):
        return self.recomendacion

# Modelo para Laboratorio
class Laboratorio(models.Model):
    id_laboratorio = models.AutoField('Id Laboratorio', primary_key=True)
    laboratorio = models.CharField('Laboratorio', max_length=100)

    def __str__(self):
        return self.laboratorio

# Modelo para Via_ingesta
class Via_ingesta(models.Model):
    id_via_ingesta = models.AutoField('Id Via Ingesta', primary_key=True)
    via_ingesta = models.CharField('Via Ingesta', max_length=100)

    def __str__(self):
        return self.via_ingesta


