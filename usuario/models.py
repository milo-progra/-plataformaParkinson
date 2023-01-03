from django.db import models
from django.contrib.auth.models import AbstractUser




# Create your models here.
# Modelo para Usuario
# Se elimino el , default=1 debido a que no dejaba crear un usuario administrador por que solicitaba un tipo de usuario por defecto

# Modelo para Tipo_Usuario
class Tipo_Usuario(models.Model):
    id_tipo_usuario=models.AutoField('id tipo usuario',primary_key=True)
    nombre_tipo_usuario = models.CharField('Nombre tipo usuario', max_length=100)
    descripcion=models.CharField('Descripcion', max_length=400)

    def __str__(self):
        return self.nombre_tipo_usuario



class Usuario(AbstractUser):
    tipo_usuario = models.ForeignKey(Tipo_Usuario, on_delete=models.CASCADE, verbose_name="Tipo Usuario", null=True)

    def __str__(self):
        return self.username +' / '+ str(self.tipo_usuario) + ' / '+ self.first_name +' / '+ self.last_name +' / '+ self.email
        
    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self, app_label):
        return True   

    class Meta:
        ordering = ['username']



