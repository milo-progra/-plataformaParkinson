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


# Modelo para Medicamento
class Medicamento(models.Model):
    id_medicamento = models.AutoField('Id Medicamento', primary_key=True)
    nombre_medicamento = models.CharField('Nombre Medicamento', max_length=100)
    medida_medicamento = models.IntegerField('Medida Medicamento')
    cantidad_comprimidos = models.IntegerField('Cantidad Medicamento')
    tipo_farmaco = models.ForeignKey(Tipo_farmaco, on_delete=models.CASCADE, verbose_name="Tipo_farmaco", null=True)
    forma_farmaceutica = models.ForeignKey(Forma_farmaceutica, on_delete=models.CASCADE, verbose_name="Forma_farmaceutica", null=True)
    recomendacion = models.ForeignKey(Recomendacion_consumo, on_delete=models.CASCADE, verbose_name="Recomendacion_consumo", null=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name="Marca", null=True)
    via_ingesta = models.ForeignKey(Via_ingesta, on_delete=models.CASCADE, verbose_name="Via_ingesta", null=True)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, verbose_name="Laboratorio", null=True)


    def __str__(self):
        return self.nombre_medicamento +' | '+ str(self.medida_medicamento) + ' mg'+ ' | '  + str(self.via_ingesta) + ' | ' + str(self.marca) + ' | ' + str(self.laboratorio)

    class Meta:
        ordering = ['-laboratorio']
