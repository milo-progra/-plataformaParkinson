from logging import Filter
from re import L
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import AbstractUser
from usuario.models import Usuario
from paciente.models import Diabetes, Hipertension

# Create your models here.

#Modelo para Region
class Region(models.Model):
    id_region     = models.AutoField('Id Region', primary_key=True)
    nombre_region = models.CharField('Nombre Region', max_length=100)

    def __str__(self):
        return self.nombre_region 

# Modelo para Provincia
class Provincia(models.Model):
    id_provincia     = models.AutoField('Id Provincia', primary_key=True)
    nombre_provincia = models.CharField('Nombre Provincia', max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Region", null=True)

    def __str__(self):
        return self.nombre_provincia

# Modelo para Comuna
class Comuna(models.Model):
    id_comuna       = models.AutoField('Id Comuna', primary_key=True)
    nombre_comuna   = models.CharField('Nombre Comuna', max_length=100)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, verbose_name="Provincia", null=True)
        
    def __str__(self):
        return self.nombre_comuna




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



# Modelo para Institucion
class Institucion(models.Model): 
    nombre_institucion = models.CharField('Nombre Institución', max_length=100)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, verbose_name="Comuna", null=True)
    descripcion = models.CharField('Descripción Institución',max_length=2000)
 
    def __str__(self): 
        return self.nombre_institucion +'/'+ str(self.comuna)

# Modelo para Neurologo
class Neurologo(models.Model):
    id_neurologo        = models.IntegerField('Id Usuario')
    username_neurologo  = models.OneToOneField(Usuario,on_delete=models.CASCADE, null=False, blank=False, primary_key=True) 
    rut_neurologo       = models.CharField('Rut Neurologo', max_length=10)
    nombre_neurologo    = models.CharField('Nombre Neurologo', max_length=100)
    apellido_neurologo  = models.CharField('Apellido Neurologo', max_length=100)
    direccion_neurologo = models.CharField('Direccion Neurologo', max_length=100)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, verbose_name="Institucion", null=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, verbose_name="Comuna", null=True)
    email_neurologo     = models.CharField('Email Neurologo', max_length=100)
    telefono_neurologo  = models.CharField('Telefono Neurologo', max_length=9, null=True, blank=True)
    whatsaap_neurologo  = models.CharField('Whatsaap Neurologo', max_length=9) 
    celular_neurologo   = models.CharField('Celular Neurologo', max_length=9)
    telegram_neurologo  = models.CharField('Telegram Neurologo', max_length=100, null=True, blank=True)


    def __str__(self):
        return self.nombre_neurologo + ' ' + str(self.apellido_neurologo) 
 
# Modelo para Familiar
class Familiar(models.Model):
    id_familiar         = models.IntegerField('Id Familiar')
    username_familiar   = models.OneToOneField(Usuario,on_delete=models.CASCADE, null=False, blank=False, primary_key=True)
    rut_familiar        = models.CharField('Rut Familiar', max_length=10)
    nombre_familiar     = models.CharField('Nombre Familiar', max_length=100)
    apellido_familiar   = models.CharField('Apellido Familiar', max_length=100)
    direccion_familiar  = models.CharField('Direccion Familiar', max_length=100)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, verbose_name="Comuna", null=True)
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
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, verbose_name="Comuna", null=True)
    email_paciente       = models.EmailField('Email Paciente', max_length=100)
    telefono_paciente    = models.CharField('Telefono Paciente', max_length=9, null=True, blank=True)
    whatsaap_paciente    = models.CharField('Whatsaap Paciente', max_length=9)
    celular_paciente     = models.CharField('Celular Paciente', max_length=9)
    telegram_paciente    = models.CharField('Telegram Paciente', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nombre_paciente + ' ' + str(self.apellido_paciente) 

# Modelo para Enfermera
class Enfermera(models.Model):
    id_enfermera          = models.IntegerField('Id Enfermera')
    username_enfermera    = models.OneToOneField(Usuario,on_delete=models.CASCADE, null=False, blank=False, primary_key=True)
    rut_enfermera         = models.CharField('Rut Enfermera', max_length=10)
    nombre_enfermera      = models.CharField('Nombre Enfermera', max_length=100)
    apellido_enfermera    = models.CharField('Apellido Enfermera', max_length=100)
    direccion_enfermera   = models.CharField('Direccion Enfermera', max_length=100)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, verbose_name="Comuna", null=True)
    email_enfermera       = models.EmailField('Email Enfermera', max_length=100)
    telefono_enfermera    = models.CharField('Telefono Enfermera', max_length=9, null=True, blank=True)
    whatsaap_enfermera    = models.CharField('Whatsaap Enfermera', max_length=9)
    celular_enfermera     = models.CharField('Celular Enfermera', max_length=9)
    telegram_enfermera    = models.CharField('Telegram Enfermera', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nombre_enfermera + ' ' + str(self.apellido_enfermera) 

# Modelo para Fonoaudiologo
class Fonoaudiologo(models.Model):
    id_fonoaudiologo       = models.IntegerField('Id Usuario')
    username_fonoaudiologo  = models.OneToOneField(Usuario,on_delete=models.CASCADE, null=False, blank=False, primary_key=True) 
    rut_fonoaudiologo       = models.CharField('Rut fonoaudiologo', max_length=10)
    nombre_fonoaudiologo    = models.CharField('Nombre fonoaudiologo', max_length=100)
    apellido_fonoaudiologo  = models.CharField('Apellido fonoaudiologo', max_length=100)
    direccion_fonoaudiologo = models.CharField('Direccion fonoaudiologo', max_length=100)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, verbose_name="Institucion", null=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, verbose_name="Comuna", null=True)
    email_fonoaudiologo     = models.CharField('Email fonoaudiologo', max_length=100)
    telefono_fonoaudiologo  = models.CharField('Telefono fonoaudiologo', max_length=9, null=True, blank=True)
    whatsaap_fonoaudiologo  = models.CharField('Whatsaap fonoaudiologo', max_length=9) 
    celular_fonoaudiologo   = models.CharField('Celular fonoaudiologo', max_length=9)
    telegram_fonoaudiologo  = models.CharField('Telegram fonoaudiologo', max_length=100, null=True, blank=True)


    def __str__(self):
        return self.nombre_fonoaudiologo + ' ' + str(self.apellido_fonoaudiologo) 

# Modelo para Bitacora
class Bitacora (models.Model):
    username_enfermera=models.ForeignKey(Enfermera, on_delete=models.CASCADE, verbose_name="Enfermera", null=True)
    username_paciente=models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente", null=True)
    timestamp= models.DateTimeField('Fecha Monitoreo', auto_now_add=True)
    anotaciones  = models.CharField('Anotaciones', max_length=1000, null=True, blank=True)
    
    
    def __str__(self):
        return str(self.username_paciente)+ ' / ' + str(self.timestamp)+ ' / ' + str(self.username_enfermera)+ ' / ' + str(self.anotaciones)
           
    class Meta:
        ordering = ['-timestamp']

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

# Modelo para Estado_monitoreo
class Estado_monitoreo(models.Model):
    id_estado_monitoreo = models.AutoField('Id estado Monitoreo', primary_key=True)
    valor_automonitoreo = models.IntegerField('Valor Automonitoreo')
    estado_monitoreo    = models.CharField('Estado Monitoreo', max_length=50, null=True, blank=True)

    def __str__(self):
        return self.estado_monitoreo

# Modelo para Automonitoreo
class Automonitoreo(models.Model):

    id_monitoreo  = models.AutoField('id Monitoreo', primary_key=True)
    fecha_automonitoreo = models.DateTimeField('Fecha Monitoreo', auto_now_add=True)
    estado_monitoreo = models.ForeignKey(Estado_monitoreo, on_delete=models.CASCADE, verbose_name="Estado_monitoreo", null=True)
    username_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente", null=True)

    def __str__(self):
        return str(self.username_paciente)+ ' / ' + str(self.estado_monitoreo)+ ' / ' + str(self.fecha_automonitoreo)

    class Meta:
        ordering = ['-fecha_automonitoreo']

# Modelo para Animo
class Animo(models.Model):
    id_Animo = models.AutoField('Id Animo', primary_key=True)
    valor_animo = models.IntegerField('Valor Animo')
    nombre_animo    = models.CharField('Nombre Animo', max_length=50, null=True, blank=True)
    #codigo_emoticon = models.CharField('Codigo Emoticon', max_length=50, null=True, blank=True)
    def __str__(self):
        return self.nombre_animo 
        
# Modelo para Estado_animo
class Estado_animo(models.Model):
    id_estado_animo  = models.AutoField('Id Estado Animo', primary_key=True)
    fecha_estado_animo = models.DateTimeField('Fecha Estado Animo', auto_now_add=True)
    animo = models.ForeignKey(Animo, on_delete=models.CASCADE, verbose_name="Animo", null=True)
    username_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente", null=True)

    def __str__(self):
        return str(self.username_paciente)+ ' / ' + str(self.animo) + ' / ' + str(self.fecha_estado_animo)

    class Meta:
        ordering = ['-fecha_estado_animo']
    
# Modelo para Receta
class Receta(models.Model):
    id_receta = models.AutoField('Id Receta', primary_key=True)
    fecha_receta = models.DateField('Fecha Receta',  auto_now_add=True)
    horario_medicamento = models.TimeField('Hora Medicamento', auto_now=False, auto_now_add=False)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, verbose_name="Medicamento", null=True)
    dosis = models.ForeignKey(Dosis, on_delete=models.CASCADE, verbose_name="Dosis", null=True)
    username_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente", null=True)

    def __str__(self):
        return str(self.username_paciente)+' | '+str(self.medicamento)+' | '+str(self.dosis)

    class Meta:
        ordering = ['horario_medicamento']

# Modelo para Recordatorio_grabacion
class Recordatorio_grabacion(models.Model):
    id_recordatorio = models.AutoField('Id recordatorio', primary_key=True)
    hora_recordatorio = models.TimeField('Hora Recordatorio', auto_now=False, auto_now_add=False)
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, verbose_name="Receta", null=True)

    def __str__(self):
        return self.receta +' | ' +self.hora_recordatorio

# Modelo para Descuento
class Descuento(models.Model):
    id_descuento    = models.AutoField('id Descuento', primary_key=True)
    medicamento     = models.ForeignKey(Medicamento, on_delete=models.CASCADE, verbose_name="Medicamento", null=True)
    descuento       = models.DecimalField('Descuento', max_digits=3, decimal_places=1)
    fecha_inicio    = models.DateField('Fecha Inicio', auto_now=False, auto_now_add=False)
    fecha_fin       = models.DateField('Fecha Fin', auto_now=False, auto_now_add=False)
    ticket_decuento = models.CharField('Direccion Paciente', max_length=100)

    def __str__(self):
        return self.medicamento +' | '+ self.descuento

# Modelo para Descuento_usado
class Descuento_usado(models.Model):
    id_descuento_usado    = models.AutoField('Id Descuento Usado', primary_key=True)
    descuento     = models.ForeignKey(Descuento, on_delete=models.CASCADE, verbose_name="Descuento", null=True)
    fecha_usado    = models.DateField('Fecha Usado', auto_now=False, auto_now_add=False)
    username     = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario", null=True)



    def __str__(self):
        return self.fecha_usado +' | '+ self.descuento

# Modelo para Familiar_paciente
class Familiar_paciente(models.Model):
    username_familiar = models.ForeignKey(Familiar, on_delete=models.CASCADE, verbose_name="Familiar", null=True)
    username_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente", null=True)

    def __str__(self):
        return str(self.username_familiar) +' | '+ str(self.username_paciente)

# Modelo para Neurologo_paciente
class Neurologo_paciente(models.Model):
    username_neurologo = models.ForeignKey(Neurologo, on_delete=models.CASCADE, verbose_name="Neurologo", null=True)
    username_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente", null=True)

    def __str__(self):
        return str(self.username_neurologo) +' | '+ str(self.username_paciente)

# Modelo para Fonoaudiologo_paciente
class Fonoaudiologo_paciente(models.Model):
    username_fonoaudiologo = models.ForeignKey(Fonoaudiologo, on_delete=models.CASCADE, verbose_name="Fonoaudiologo", null=True)
    username_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente", null=True)

    def __str__(self):
        return str(self.username_fonoaudiologo) +' | '+ str(self.username_paciente)

# Modelo para Enfermera_paciente
class Enfermera_paciente(models.Model):
    username_enfermera = models.ForeignKey(Enfermera, on_delete=models.CASCADE, verbose_name="Enfermera", null=True)
    username_paciente  = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente", null=True)

    def __str__(self):
        return str(self.username_enfermera) +' | '+ str(self.username_paciente)

# Modelo para Enfermera_neurologo
class Enfermera_neurologo(models.Model):
    username_enfermera = models.ForeignKey(Enfermera, on_delete=models.CASCADE, verbose_name="Enfermera", null=True)
    username_neurologo  = models.ForeignKey(Neurologo, on_delete=models.CASCADE, verbose_name="Neurologo", null=True)

    def __str__(self):
        return str(self.username_enfermera) +' | '+ str(self.username_neurologo)

# Modelo para Documento
class Documento(models.Model):
    id_documento   = models.AutoField('Id Documento', primary_key=True)
    titulo    = models.CharField('Titulo', max_length=1000)
    documento      = models.FileField(upload_to='documentos/')
    descripcion    = models.CharField('Descripcion', max_length=1000)
    qr = models.FileField(upload_to='qr_documento/', null=True, blank=True)

    def __str__(self):
        return self.titulo

# Modelo para Paciente_Documento
class Paciente_Documento(models.Model):
    id_paciente_documento   = models.AutoField('Id Documento', primary_key=True)
    documento      =   models.ForeignKey(Documento, on_delete=models.CASCADE, verbose_name="Documento", null=True)
    username_paciente    = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente", null=True)
    autorizado = models.BooleanField(default=True)    
    timestamp = models.DateTimeField('Fecha Autorizacion', auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return str(self.documento) +' | '+ str(self.username_paciente) + '|' + str(self.timestamp)

# Modelo para Preregistro
class Preregistro(models.Model):
    nombre_paciente    = models.CharField('Nombre', max_length=100)
    apellido_paciente    = models.CharField('Apellido', max_length=100)
    rut_paciente    = models.CharField('Rut', max_length=10)
    telefono_paciente  = models.CharField('Telefono paciente', max_length=9, null=True, blank=True)
    email_paciente       = models.EmailField('Email paciente', max_length=100)
    neurologo     = models.ForeignKey(Neurologo, on_delete=models.CASCADE, verbose_name="Neurologo de Referencia", null=True)
    timestamp = models.DateTimeField('Fecha Prere4gistro', auto_now_add=True, null=True, blank=True)

    

    def __str__(self):
        return self.nombre_paciente

    class Meta:
        ordering = ['-timestamp']

# Modelo para RegistroCorreos
class RegistroCorreos(models.Model): 
    asunto = models.CharField(max_length=1400) 
    mensaje = models.CharField(max_length=1400) 
    dirigido = models.CharField(max_length=1400) 
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True) 
 
    def __str__(self): 
        return self.asunto

    class Meta:
        ordering = ['-timestamp']


