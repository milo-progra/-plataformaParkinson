from django.urls import path, include
from .views import lista_medicamentos, editar_medicamento, admin_medicamento

urlpatterns = [
        path('lista_medicamentos/', lista_medicamentos, name="lista_medicamentos"),
        path('editar_medicamento/<id_medicamento>', editar_medicamento, name="editar_medicamento"),
        path('admin_medicamento/', admin_medicamento, name="admin_medicamento"),
]
