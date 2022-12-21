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

# Modelo para Familiar
class Familiar(models.Model):
    id_familiar         = models.IntegerField('Id Familiar')
    username_familiar   = models.OneToOneField(Usuario,on_delete=models.CASCADE, null=False, blank=False, primary_key=True)
    rut_familiar        = models.CharField('Rut Familiar', max_length=10)
    nombre_familiar     = models.CharField('Nombre Familiar', max_length=100)
    apellido_familiar   = models.CharField('Apellido Familiar', max_length=100)
    direccion_familiar  = models.CharField('Direccion Familiar', max_length=100)
    comuna              = models.ForeignKey(to='app.comuna', on_delete=models.CASCADE, null=True)
    email_familiar      = models.CharField('Email Familiar', max_length=100)
    telefono_familiar   = models.CharField('Telefono Familiar', max_length=9, null=True, blank=True)
    whatsaap_familiar   = models.CharField('Whatsaap Familiar', max_length=9)
    celular_familiar    = models.CharField('Celular Familiar', max_length=9)
    telegram_familiar   = models.CharField('Telegram Familiar', max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.nombre_familiar + ' ' + str(self.apellido_familiar) 



# Modelo para Paciente
class Paciente(models.Model):
    id_paciente          = models.IntegerField('Id Paciente')
    username_paciente    = models.OneToOneField(Usuario,on_delete=models.CASCADE, null=False, blank=False, primary_key=True)
    rut_paciente         = models.CharField('Rut Paciente', max_length=10)
    nombre_paciente      = models.CharField('Nombre Paciente', max_length=100)
    apellido_paciente    = models.CharField('Apellido Paciente', max_length=100)
    diabetes             = models.ForeignKey(Diabetes, on_delete=models.CASCADE, verbose_name="Diabetes", null=True)
    hipertension         = models.ForeignKey(Hipertension, on_delete=models.CASCADE, verbose_name="Hipertension", null=True)
    direccion_paciente   = models.CharField('Direccion Paciente', max_length=100)
    comuna = models.ForeignKey(to='app.comuna', on_delete=models.CASCADE, verbose_name="Comuna", null=True)
    email_paciente       = models.EmailField('Email Paciente', max_length=100)
    telefono_paciente    = models.CharField('Telefono Paciente', max_length=9, null=True, blank=True)
    whatsaap_paciente    = models.CharField('Whatsaap Paciente', max_length=9)
    celular_paciente     = models.CharField('Celular Paciente', max_length=9)
    telegram_paciente    = models.CharField('Telegram Paciente', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nombre_paciente + ' ' + str(self.apellido_paciente) 
