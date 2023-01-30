
from django.shortcuts import render
from medicamento.models import MedicamentosFull 
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from .models import *
from rest_framework import viewsets, permissions


from .serializers import *

# class MedicamentoFullViewSet(viewsets.ModelViewSet):
#     queryset = MedicamentosFull.objects.all()
#     #permission_classes =[permissions.IsAdminUser]
#     serializer_class= MedicamentoFullSerializer

#     #funcion para filtrar medicamentos por sucursal
#     def get_queryset(self):
#         #La variable medicamento guardara todo los medicamentos
#         medicamentos = MedicamentosFull.objects.all()
#         #Guardamos el parametro de la sucursal definida en la url
#         sucursal = self.request.GET.get('sucursal')
#         # si se definio el parametro sucursal en la url
#         if sucursal:
#             medicamentos = medicamentos.filter(sucursal = sucursal)
#         return medicamentos

#     #Esta es la funcion put
#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)

#         return Response(serializer.data)
#------------ Pruebas  api rest ----------------------------------------------------------------

class MedicamentoFullViewSet(APIView):
    #permission_classes =[permissions.IsAdminUser]
    serializer_class= MedicamentoFullSerializer
    #funcion para filtrar medicamentos por sucursal
    def get(self, request,pk=None):
        #La variable medicamento guardara todo los medicamentos
        medicamentos = MedicamentosFull.objects.all()
        #Guardamos el parametro de la sucursal definida en la url
        sucursal = request.GET.get('sucursal')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')       
        #imprimo el body
        print(request.data)
        print(sucursal)
        if sucursal:
            medicamentos = MedicamentosFull.objects.filter(sucursal = sucursal)
        # si se definio el parametro sucursal en la 
        #many = True vendran varios registros
        return Response(MedicamentoFullSerializer(medicamentos, many = True).data)

    def put(self, request,pk=None):
        #Guardar el parametro ingresado en la url con el nombre /?sucursal
        sucursal = request.GET.get('sucursal')
    
        if not sucursal:
            return Response([])
        medicamentos = MedicamentosFull.objects.filter(sucursal = sucursal) 
        #guardo en la variable el query params del body con el nombre stockDiario
        arrayStockDiario = request.data.get("stockDiario")
        print(request.data)
        b = 0
        for medicamento in medicamentos:
            print(arrayStockDiario[b])
            medicamento.stockDiario = arrayStockDiario[b]   
            b = b +1
            medicamento.save()
        # si se definio el parametro sucursal en la url
        return Response(MedicamentoFullSerializer(medicamentos, many = True).data)