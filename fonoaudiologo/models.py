from django.db import models
from usuario.models import Usuario
from medico_y_enfermera.models import Institucion 
from django.db import models
from paciente.models import Paciente
# Create your models here.
# Modelo para Fonoaudiologo
class Fonoaudiologo(models.Model):
    id_fonoaudiologo       = models.IntegerField('Id Usuario')
    username_fonoaudiologo  = models.OneToOneField(Usuario,on_delete=models.CASCADE, null=False, blank=False, primary_key=True) 
    rut_fonoaudiologo       = models.CharField('Rut fonoaudiologo', max_length=10)
    nombre_fonoaudiologo    = models.CharField('Nombre fonoaudiologo', max_length=100)
    apellido_fonoaudiologo  = models.CharField('Apellido fonoaudiologo', max_length=100)
    direccion_fonoaudiologo = models.CharField('Direccion fonoaudiologo', max_length=100)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, verbose_name="Institucion", null=True)
    comuna = models.ForeignKey(to='app.comuna', on_delete=models.CASCADE, verbose_name="Comuna", null=True)
    email_fonoaudiologo     = models.CharField('Email fonoaudiologo', max_length=100)
    telefono_fonoaudiologo  = models.CharField('Telefono fonoaudiologo', max_length=9, null=True, blank=True)
    whatsaap_fonoaudiologo  = models.CharField('Whatsaap fonoaudiologo', max_length=9) 
    celular_fonoaudiologo   = models.CharField('Celular fonoaudiologo', max_length=9)
    telegram_fonoaudiologo  = models.CharField('Telegram fonoaudiologo', max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.nombre_fonoaudiologo + ' ' + str(self.apellido_fonoaudiologo) 



# Modelo para Fonoaudiologo_paciente
class Fonoaudiologo_paciente(models.Model):
    username_fonoaudiologo = models.ForeignKey(Fonoaudiologo, on_delete=models.CASCADE, verbose_name="Fonoaudiologo", null=True)
    username_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente", null=True)

    def __str__(self):
        return str(self.username_fonoaudiologo) +' | '+ str(self.username_paciente)
