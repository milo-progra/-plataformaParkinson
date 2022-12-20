from nturl2path import url2pathname
from pathlib import Path
from django.urls import path
from .views import *
from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register('api/familiar', FamiliarViewSet, 'familiar')
router.register('api/receta', RecetaViewSet, 'receta')
router.register('api/audio', AudioViewSet, 'audio')
app_name="app"
urlpatterns = router.urls
