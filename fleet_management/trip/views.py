from rest_framework import viewsets
from .models import Trip
from .serializers import TripSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]