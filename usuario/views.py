from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.template.loader import render_to_string
from django.views.generic import View
from.forms import *
from django.contrib import messages
from app.models import Paciente
import io
from django.http import FileResponse
from .utils import render_to_pdf



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



class GetPdf(View):
    
    def get (self, *args, **kwargs):
        data = {

        }
        pdf = render_to_pdf('condiciones_de_uso/condiciones.html',data)
        return HttpResponse(pdf, content_type = 'application/pdf')
    
