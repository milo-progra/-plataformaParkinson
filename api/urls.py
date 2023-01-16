from nturl2path import url2pathname
from pathlib import Path
from django.urls import path, re_path
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register('medicamento_full', MedicamentoFullViewSet, 'medicamento_full')


#El operador += en x+=1 es equivalente a x=x+1
urlpatterns = router.urls