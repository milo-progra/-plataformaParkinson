from django.urls import path, include
from .views import fonoaudiologo_paciente, fonoaudiologo_info_paciente, audio_paciente, vocalizacion, intensidad

urlpatterns = [
    path('fonoaudiologo_paciente/', fonoaudiologo_paciente, name="fonoaudiologo_paciente"),
    path('fonoaudiologo_info_paciente/<username_paciente_id>' , fonoaudiologo_info_paciente, name="fonoaudiologo_info_paciente"),
    path('audio_paciente/<username_paciente_id>', audio_paciente, name="audio_paciente"),
    path('vocalizacion/<username_paciente_id>', vocalizacion, name="vocalizacion"),
    path('intensidad/<username_paciente_id>', intensidad, name="intensidad"),
]
