from django.shortcuts import render
from .models import Fonoaudiologo_paciente, Audio
from paciente.models import Paciente
#Cambiar  el modelo Famliar_paciente, Receta al modulo paciente
from app.models import Familiar_paciente, Receta, Estado_animo, Automonitoreo, Vocalizacion, Intensidad


#vista de los pacientes que tiene cada fonoaudiologo
def fonoaudiologo_paciente(request):
    fonoaudiologo_pacientes=Fonoaudiologo_paciente.objects.all().filter(username_fonoaudiologo=request.user.id)
   
    return render(request, 'pacientes_fono/fonoaudiologo_paciente.html',{'fonoaudiologo_pacientes':fonoaudiologo_pacientes})


#informacion del paciente seleccionado por el fonoaudiologo
def fonoaudiologo_info_paciente(request,username_paciente_id):
    pacientes=Paciente.objects.all().filter(username_paciente=username_paciente_id)
    fonoaudiologo_pacientes=Fonoaudiologo_paciente.objects.all().filter(username_paciente_id=username_paciente_id)
    familiar_pacientes=Familiar_paciente.objects.all().filter(username_paciente_id=username_paciente_id)
    receta=Receta.objects.all().filter(username_paciente_id=username_paciente_id)
    estado_animos = Estado_animo.objects.all().filter(username_paciente_id=username_paciente_id)
    automonitoreo=Automonitoreo.objects.all().filter(username_paciente_id=username_paciente_id)
    return render(request, 'pacientes_fono/fonoaudiologo_info_paciente.html',{'automonitoreo':automonitoreo,'estado_animos':estado_animos,'receta':receta,'familiar_pacientes':familiar_pacientes,'pacientes':pacientes,'fonoaudiologo_pacientes':fonoaudiologo_pacientes})


#audios del paciente en vista fonoaudiologo
def audio_paciente(request,username_paciente_id):
    audios=Audio.objects.all().filter(username_paciente_id=username_paciente_id)
    pacientes=Paciente.objects.all().filter(username_paciente_id=username_paciente_id)
    return render(request, 'pacientes_fono/audio_paciente.html',{'audios':audios,'pacientes':pacientes})


#Vocalicaciones del paciente
def vocalizacion(request,username_paciente_id):
    vocalizacion=Vocalizacion.objects.all().filter(username_paciente_id=username_paciente_id)
    pacientes=Paciente.objects.all().filter(username_paciente_id=username_paciente_id)
    return render(request, 'pacientes_fono/vocalizacion.html',{'vocalizacion':vocalizacion,'pacientes':pacientes})


#intensidad del paciente
def intensidad(request,username_paciente_id):
    intensidad=Intensidad.objects.all().filter(username_paciente_id=username_paciente_id)
    pacientes=Paciente.objects.all().filter(username_paciente_id=username_paciente_id)
    return render(request, 'pacientes_fono/intensidad.html',{'intensidad':intensidad,'pacientes':pacientes})