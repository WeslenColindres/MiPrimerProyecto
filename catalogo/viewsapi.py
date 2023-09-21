from rest_framework import viewsets, permissions
from .serializers import PaisSerializer, DepartamentoSerializer, MunicipioSerializer
from .models import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    permission_classes = [permissions.IsAuthenticated]  
    serializer_class = PaisSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DepartamentoSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MunicipioSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]