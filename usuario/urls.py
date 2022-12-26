from django.urls import path, include
from .views import pre_registro

urlpatterns = [
        path('preregistro/', pre_registro, name="preregistro"),
]
