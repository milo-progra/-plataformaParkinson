from django.contrib import admin
from .models import Tipo_Usuario, Usuario
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

admin.site.register(Usuario, BaseUserAdmin)
admin.site.register(Tipo_Usuario)
