from rest_framework import serializers
from .models import FinanceApplication, Contact


class FinanceApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceApplication
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'