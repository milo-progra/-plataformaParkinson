from django.shortcuts import render, redirect
from medicamento.models import *
from .forms import FormMedicamento, FormMedicamentosFull
# Create your views here.
#listado medicamentos
def lista_medicamentos(request):
    medicamentos = Medicamento.objects.all()
    
    return render(request, 'enfermeras/lista_medicamentos.html',{'medicamentos':medicamentos})



#vista de administrador para ver los medicamentos
def admin_medicamento(request):
    medicamentos=Medicamento.objects.all()
    return render(request, 'administrador/admin_medicamento.html',{'medicamentos':medicamentos})



#Vista de administrador para editar medicamento
def editar_medicamento(request, id_medicamento):
    medicamento = Medicamento.objects.get(id_medicamento=id_medicamento)
    medicamentos = Medicamento.objects.all().filter(id_medicamento=id_medicamento)
    formulario = FormMedicamento(request.POST or None,  instance=medicamento)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('admin_medicamento')
    return render(request, 'administrador/editar_medicamento.html', {'formulario': formulario, 'medicamentos': medicamentos})    



def agregar_medicamento(request):
    data = {
        'form': FormMedicamento
    }
    if request.method == 'POST':
        formulario =FormMedicamento(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='admin_medicamento')
            
        else:
            data["form"] = formulario  

    return render(request,'administrador/agregar_medicamento.html',data)


 #--------------------------------- medicuamentos full ------------------------------------------------------------


 #vista de administrador para ver los medicamentos
def admin_medicamento_full(request):
    medicamentos=MedicamentosFull.objects.all()
    data = {
        'medicamentos': medicamentos
    }
    return render(request, 'administrador/admin_medicamentos_full.html', data)


def agregar_medicamento_full(request):
    data = {
        'form': FormMedicamentosFull
    }
    if request.method == 'POST':
        formulario =FormMedicamentosFull(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='admin_medicamento_full')
            
        else:
            data["form"] = formulario  

    return render(request,'administrador/agregar_medicamento_full.html',data)



def editar_medicamento_full(request, id_medicamento):
    medicamento = MedicamentosFull.objects.get(id_medicamento=id_medicamento)
    medicamentos = MedicamentosFull.objects.all().filter(id_medicamento=id_medicamento)
    formulario = FormMedicamentosFull(request.POST or None,  instance=medicamento)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('admin_medicamento_full')
    return render(request, 'administrador/editar_medicamento_full.html', {'formulario': formulario, 'medicamentos': medicamentos})    

