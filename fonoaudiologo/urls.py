from django.urls import path, include
from .views import fonoaudiologo_paciente, fonoaudiologo_info_paciente

urlpatterns = [
    path('fonoaudiologo_paciente/', fonoaudiologo_paciente, name="fonoaudiologo_paciente"),
    path('fonoaudiologo_info_paciente/<username_paciente_id>' , fonoaudiologo_info_paciente, name="fonoaudiologo_info_paciente"),
]
