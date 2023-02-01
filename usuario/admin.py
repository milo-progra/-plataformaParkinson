from django.contrib import admin
from .models import Tipo_Usuario, Usuario
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import AdminFormaActualizar, AdminFormaCreacionUsuario
# Register your models here.
class UserAdmin(BaseUserAdmin):
    
    form = AdminFormaActualizar
    add_form = AdminFormaCreacionUsuario


    #list_display = ('email', 'username')
    list_filter = ('email',)
    fieldsets = (
        (None,{'fields': ('username','email', 'password')}),
        ('Informacion personal', {'fields': ( 'first_name', 'last_name', 'tipo_usuario')}),
        ('Permisos Django', {'fields': ('is_staff', 'is_active', 'groups')})

    )

    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('username','password1', 'password2')
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)
    list_display = ("username", "id","email", "first_name", "last_name", "is_staff")



admin.site.register(Usuario, UserAdmin)
admin.site.register(Tipo_Usuario)
