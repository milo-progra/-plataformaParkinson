from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import fonoaudiologo_paciente, fonoaudiologo_info_paciente, audio_paciente, vocalizacion, intensidad

urlpatterns = [
    path('fonoaudiologo_paciente/', login_required(fonoaudiologo_paciente), name="fonoaudiologo_paciente"),
    path('fonoaudiologo_info_paciente/<username_paciente_id>' ,login_required(fonoaudiologo_info_paciente), name="fonoaudiologo_info_paciente"),
    path('audio_paciente/<username_paciente_id>', login_required(audio_paciente), name="audio_paciente"),
    path('vocalizacion/<username_paciente_id>', login_required(vocalizacion), name="vocalizacion"),
    path('intensidad/<username_paciente_id>', login_required(intensidad), name="intensidad"),
]
