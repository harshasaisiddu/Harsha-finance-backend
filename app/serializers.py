from rest_framework import serializers
from .models import Category, FinanceApplication, Contact, Tags, Vehicle, VehicleDetails


class FinanceApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceApplication
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    vehicle_name = serializers.CharField(source='vehicle.name', read_only=True)
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


class CategorySerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(
        source="name",
        read_only=True
    )

    class Meta:
        model = Category
        fields = "__all__"


class TagsSerializer(serializers.ModelSerializer):
    tag_name = serializers.CharField(
        source="name",
        read_only=True
    )

    class Meta:
        model = Tags
        fields = "__all__"