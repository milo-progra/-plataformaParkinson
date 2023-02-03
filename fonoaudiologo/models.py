from django.db import models
from usuario.models import Usuario
from medico_y_enfermera.models import Institucion 
from django.db import models
from paciente.models import Paciente
# Create your models here.

class Fonoaudiologo(models.Model):
    id_fonoaudiologo        = models.IntegerField('Id Usuario')
    username_fonoaudiologo  = models.OneToOneField(Usuario,on_delete=models.CASCADE, null=False, blank=False, primary_key=True, limit_choices_to={'tipo_usuario':4}) 
    rut_fonoaudiologo       = models.CharField('Rut fonoaudiologo', max_length=10, unique=True)
    nombre_fonoaudiologo    = models.CharField('Nombre fonoaudiologo', max_length=100)
    apellido_fonoaudiologo  = models.CharField('Apellido fonoaudiologo', max_length=100)
    direccion_fonoaudiologo = models.CharField('Direccion fonoaudiologo', max_length=100)
    institucion             = models.ForeignKey(Institucion, on_delete=models.CASCADE, verbose_name="Institucion", null=True)
    comuna                  = models.ForeignKey(to='app.comuna', on_delete=models.CASCADE, verbose_name="Comuna", null=True)
    email_fonoaudiologo     = models.CharField('Email fonoaudiologo', max_length=100, unique=True)
    telefono_fonoaudiologo  = models.CharField('Telefono fonoaudiologo', max_length=9, null=True, blank=True)
    whatsaap_fonoaudiologo  = models.CharField('Whatsaap fonoaudiologo', max_length=9) 
    celular_fonoaudiologo   = models.CharField('Celular fonoaudiologo', max_length=9)
    telegram_fonoaudiologo  = models.CharField('Telegram fonoaudiologo', max_length=100, null=True, blank=True, unique=True)
    
    def __str__(self):
        return self.id_fonoaudiologo + '/' + self.nombre_fonoaudiologo + ' ' + str(self.apellido_fonoaudiologo) 



# Modelo para Fonoaudiologo_paciente
class Fonoaudiologo_paciente(models.Model):
    username_fonoaudiologo = models.ForeignKey(Fonoaudiologo, on_delete=models.CASCADE, verbose_name="Fonoaudiologo", null=True)
    username_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente", null=True)

    def __str__(self):
        return str(self.username_fonoaudiologo) +' | '+ str(self.username_paciente)



# Modelo para Audio
class Audio (models.Model):
    username_paciente=models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente", null=True)
    timestamp= models.DateTimeField('Fecha Monitoreo', auto_now_add=True)
    url_archivo_audio=models.FileField(upload_to='audios/')
    jitter_ppq5=models.IntegerField('jitter ppq5', null=True)
    jitter_rap=models.IntegerField('jitter rap', null=True)
    maximum_pitch=models.IntegerField('maximum pitch', null=True)   
    error_jitter_ppq5=models.IntegerField('error jitter ppq5', null=True)
    error_jitter_rap=models.IntegerField('error jitter rap', null=True)
    error_maximum_pitch=models.IntegerField('error maximum pitch', null=True)

    jitter_ppq5_IA          =       models.IntegerField('jitter ppq5', null=True)
    jitter_rap_IA           =       models.IntegerField('jitter rap', null=True)
    maximum_pitch_IA        =       models.IntegerField('maximum pitch', null=True)   
    error_jitter_ppq5_IA    =       models.IntegerField('error jitter ppq5', null=True)
    error_jitter_rap_IA     =       models.IntegerField('error jitter rap', null=True)
    error_maximum_pitch_IA  =       models.IntegerField('error maximum pitch', null=True)

    def __str__(self):
        return str(self.username_paciente)+ ' / ' + str(self.timestamp)+ ' / ' + str(self.url_archivo_audio)+ ' / ' + str(self.jitter_ppq5)+ ' / ' + str(self.jitter_rap)+ ' / ' + str(self.maximum_pitch)+ ' / ' + str(self.error_jitter_ppq5)+ ' / ' + str(self.error_jitter_rap)+ ' / ' + str(self.error_maximum_pitch)
           
    class Meta:
        ordering = ['-timestamp']


# Modelo para Vocalizacion
class Vocalizacion (models.Model):
    username_paciente=models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente", null=True)
    timestamp= models.DateTimeField('Fecha Monitoreo', auto_now_add=True)
    url_archivo_vocalizacion=models.FileField(upload_to='vocalizacion/')
    duracion=models.IntegerField('Duracion', null=True)
    bpminute=models.IntegerField('BPM Beats Per Minute ', null=True)
    bpmeasure=models.IntegerField('Beats Per Measure', null=True)   
    comentario=models.CharField( 'Comentarios',max_length=500, null=True)
    
    
    def __str__(self):
        return str(self.username_paciente)+ ' / ' + str(self.timestamp)+ ' / ' + str(self.url_archivo_vocalizacion)+ ' / ' + str(self.duracion)+ ' / ' + str(self.bpminute)+ ' / ' + str(self.bpmeasure)+ ' / ' + str(self.comentario)
           
    class Meta:
        ordering = ['-timestamp']

# Modelo para Intensidad
class Intensidad (models.Model):
    username_paciente=models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente", null=True)
    timestamp= models.DateTimeField('Fecha Monitoreo', auto_now_add=True)
    url_archivo_intensidad=models.FileField(upload_to='intensidad/')
    intensidad=models.IntegerField('Intensidad', null=True)
    mindb=models.IntegerField('Min dB', null=True)
    maxdb=models.IntegerField('Max dB', null=True)   
    comentario=models.CharField( 'Comentarios',max_length=500, null=True)
    
    def __str__(self):
        return str(self.username_paciente)+ ' / ' + str(self.timestamp)+ ' / ' + str(self.url_archivo_intensidad
        )+ ' / ' + str(self.intensidad)+ ' / ' + str(self.mindb)+ ' / ' + str(self.maxdb)+ ' / ' + str(self.comentario)
           
    class Meta:
        ordering = ['-timestamp']        