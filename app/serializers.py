from rest_framework import serializers
from .models import FinanceApplication, Contact, Vehicle, VehicleDetails


class FinanceApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceApplication
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'name']
        
class VehicleDetailsSerializer(serializers.ModelSerializer):

    vehicle_name = serializers.CharField(
        source="vehicle.name",
        read_only=True
    )

    class Meta:
        model = VehicleDetails
        fields = "__all__"