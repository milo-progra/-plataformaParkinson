from .models import *
from rest_framework import viewsets, permissions
from .serializers import *

class FamiliarViewSet(viewsets.ModelViewSet):
    queryset = Familiar.objects.all()
    permission_classes =[permissions.IsAdminUser]
    serializer_class= FamiliarSerializer

class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all()
    permission_classes =[permissions.IsAdminUser]
    serializer_class= RecetaSerializer

class AudioViewSet(viewsets.ModelViewSet):
    queryset = Audio.objects.all()
    permission_classes =[permissions.IsAdminUser]
    serializer_class= AudioSerializer