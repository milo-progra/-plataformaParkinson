from nturl2path import url2pathname
from pathlib import Path
from django.urls import path
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()

router.register('medicamento_full', MedicamentoFullViewSet, 'medicamento_full')

urlpatterns = router.urls
