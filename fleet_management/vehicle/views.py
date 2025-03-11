from rest_framework import viewsets
from .models import Vehicle
from .serializers import VehicleSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
