from django.shortcuts import render
from medicamento.models import MedicamentosFull 
# Create your views here.
from .models import *
from rest_framework import viewsets, permissions
from .serializers import *

class MedicamentoFullViewSet(viewsets.ModelViewSet):
    queryset = MedicamentosFull.objects.all()
    permission_classes =[permissions.IsAdminUser]
    serializer_class= MedicamentoFullSerializer