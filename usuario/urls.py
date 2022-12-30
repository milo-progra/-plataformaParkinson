from django.urls import path, include
from .views import pre_registro, GetPdf

urlpatterns = [
        path('preregistro/', pre_registro, name="preregistro"),
      
        path('pdf_condiciones_de_uso', GetPdf.as_view(), name='pdf_conciciones_de_uso')
]
