from rest_framework import serializers
from .models import Vehicle
from fleet_management.trip.serializers import TripSerializer

class VehicleSerializer(serializers.ModelSerializer):
    trips=TripSerializer(many=True,required=False)
    class Meta:
        model = Vehicle
        fields = ['id','plate','model','color','trips']