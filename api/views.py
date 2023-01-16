from django.shortcuts import render
from medicamento.models import MedicamentosFull 
from rest_framework import generics
# Create your views here.
from .models import *
from rest_framework import viewsets, permissions
from .serializers import *

class MedicamentoFullViewSet(viewsets.ModelViewSet):
    queryset = MedicamentosFull.objects.all()
    #permission_classes =[permissions.IsAdminUser]
    serializer_class= MedicamentoFullSerializer
    def get_queryset(self):
        #La variable medicamento guardara todo los medicamentos
        medicamentos = MedicamentosFull.objects.all()
        #Guardamos el parametro de la sucursal definida en la url
        sucursal = self.request.GET.get('sucursal')
        # si se definio el parametro sucursal en la url
        if sucursal:
            medicamentos = medicamentos.filter(sucursal = sucursal)
        
        return medicamentos



                       