from django.urls import path, include
from .views import *

urlpatterns = [
        path('lista_medicamentos/', lista_medicamentos, name="lista_medicamentos"),
        path('editar_medicamento/<id_medicamento>', editar_medicamento, name="editar_medicamento"),
        path('admin_medicamento/', admin_medicamento, name="admin_medicamento"),
        path('agregar_medicamento/', agregar_medicamento, name='agregar_medicamento'),
        #------- medicamentos full --------------------------------------------------------
        path('admin_medicamento_full', admin_medicamento_full, name='admin_medicamento_full'),
        path('agregar_medicamento_full', agregar_medicamento_full, name='agregar_medicamento_full'),
        path('editar_medicamento_full/<id_medicamento>', editar_medicamento_full, name="editar_medicamento_full"),
       
]
