from django.urls import path, include
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
        path('lista_medicamentos/', login_required(lista_medicamentos), name="lista_medicamentos"),
        path('editar_medicamento/<id_medicamento>',login_required(editar_medicamento), name="editar_medicamento"),
        path('admin_medicamento/', login_required(admin_medicamento), name="admin_medicamento"),
        path('agregar_medicamento/',login_required(agregar_medicamento), name='agregar_medicamento'),
        #------- medicamentos full --------------------------------------------------------
        path('admin_medicamento_full', login_required( admin_medicamento_full), name='admin_medicamento_full'),
        path('agregar_medicamento_full', login_required(agregar_medicamento_full), name='agregar_medicamento_full'),
        path('editar_medicamento_full/<id_medicamento>',login_required(editar_medicamento_full), name="editar_medicamento_full"),
       
]
