from django.shortcuts import render, redirect, get_object_or_404
from.forms import *
from django.contrib import messages
from app.models import Paciente



#preregistro del paciente
def pre_registro(request):
    data= {
        'form':FormPreregistro()
    }
    if request.method == 'POST':
        formulario=FormPreregistro(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            
            messages.success(request, "Gracias por su inscripción")
            return redirect(to="index")
        data['form']=formulario
    return render(request,'registration/registro.html',data)



