from django.shortcuts import render
from .models import Fonoaudiologo_paciente
from paciente.models import Paciente
#Cambiar  el modelo Famliar_paciente, Receta al modulo paciente
from app.models import Familiar_paciente, Receta, Estado_animo, Automonitoreo


#vista de los pacientes que tiene cada fonoaudiologo
def fonoaudiologo_paciente(request):
    fonoaudiologo_pacientes=Fonoaudiologo_paciente.objects.all().filter(username_fonoaudiologo=request.user.id)
   
    return render(request, 'fonoaudiologo/fonoaudiologo_paciente.html',{'fonoaudiologo_pacientes':fonoaudiologo_pacientes})


#informacion del paciente seleccionado por el fonoaudiologo
def fonoaudiologo_info_paciente(request,username_paciente_id):
    pacientes=Paciente.objects.all().filter(username_paciente=username_paciente_id)
    fonoaudiologo_pacientes=Fonoaudiologo_paciente.objects.all().filter(username_paciente_id=username_paciente_id)
    familiar_pacientes=Familiar_paciente.objects.all().filter(username_paciente_id=username_paciente_id)
    receta=Receta.objects.all().filter(username_paciente_id=username_paciente_id)
    estado_animos = Estado_animo.objects.all().filter(username_paciente_id=username_paciente_id)
    automonitoreo=Automonitoreo.objects.all().filter(username_paciente_id=username_paciente_id)
    return render(request, 'fonoaudiologo/fonoaudiologo_info_paciente.html',{'automonitoreo':automonitoreo,'estado_animos':estado_animos,'receta':receta,'familiar_pacientes':familiar_pacientes,'pacientes':pacientes,'fonoaudiologo_pacientes':fonoaudiologo_pacientes})
