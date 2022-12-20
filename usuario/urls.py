from django.urls import path, include
from .views import registro

urlpatterns = [
        path('preregistro/', registro, name="preregistro"),
]
