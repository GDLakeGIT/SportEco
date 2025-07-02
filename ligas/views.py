
from rest_framework import viewsets, permissions
from .models import Deporte, Federacion, Liga
from .serializers import DeporteSerializer, FederacionSerializer, LigaSerializer

class DeporteViewSet(viewsets.ModelViewSet):
    queryset = Deporte.objects.all()
    serializer_class = DeporteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class FederacionViewSet(viewsets.ModelViewSet):
    queryset = Federacion.objects.all()
    serializer_class = FederacionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LigaViewSet(viewsets.ModelViewSet):
    queryset = Liga.objects.all()
    serializer_class = LigaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
