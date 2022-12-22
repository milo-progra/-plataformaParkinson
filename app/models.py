from logging import Filter
from re import L
from tokenize import blank_re
from django.db import models
from usuario.models import Usuario
from paciente.models import Diabetes, Hipertension, Animo, Familiar, Paciente
from medico_y_enfermera.models import Institucion
from medicamento.models import Dosis, Medicamento
from fonoaudiologo.models import  Audio, Vocalizacion, Intensidad


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






# Modelo para Neurologo
class Neurologo(models.Model):
    id_neurologo        = models.IntegerField('Id Usuario')
    username_neurologo  = models.OneToOneField(Usuario,on_delete=models.CASCADE, null=False, blank=False, primary_key=True) 
    rut_neurologo       = models.CharField('Rut Neurologo', max_length=10)
    nombre_neurologo    = models.CharField('Nombre Neurologo', max_length=100)
    apellido_neurologo  = models.CharField('Apellido Neurologo', max_length=100)
    direccion_neurologo = models.CharField('Direccion Neurologo', max_length=100)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, verbose_name="Institucion", null=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, null=True)
    email_neurologo     = models.CharField('Email Neurologo', max_length=100)
    telefono_neurologo  = models.CharField('Telefono Neurologo', max_length=9, null=True, blank=True)
    whatsaap_neurologo  = models.CharField('Whatsaap Neurologo', max_length=9) 
    celular_neurologo   = models.CharField('Celular Neurologo', max_length=9)
    telegram_neurologo  = models.CharField('Telegram Neurologo', max_length=100, null=True, blank=True)


    def __str__(self):
        return self.nombre_neurologo + ' ' + str(self.apellido_neurologo) 
 



# Modelo para Enfermera
class Enfermera(models.Model):
    id_enfermera          = models.IntegerField('Id Enfermera')
    username_enfermera    = models.OneToOneField(Usuario,on_delete=models.CASCADE, null=False, blank=False, primary_key=True)
    rut_enfermera         = models.CharField('Rut Enfermera', max_length=10)
    nombre_enfermera      = models.CharField('Nombre Enfermera', max_length=100)
    apellido_enfermera    = models.CharField('Apellido Enfermera', max_length=100)
    direccion_enfermera   = models.CharField('Direccion Enfermera', max_length=100)
    comuna      = models.ForeignKey(Comuna, on_delete=models.CASCADE, verbose_name="Comuna", null=True)
    email_enfermera       = models.EmailField('Email Enfermera', max_length=100)
    telefono_enfermera    = models.CharField('Telefono Enfermera', max_length=9, null=True, blank=True)
    whatsaap_enfermera    = models.CharField('Whatsaap Enfermera', max_length=9)
    celular_enfermera     = models.CharField('Celular Enfermera', max_length=9)
    telegram_enfermera    = models.CharField('Telegram Enfermera', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nombre_enfermera + ' ' + str(self.apellido_enfermera) 



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


