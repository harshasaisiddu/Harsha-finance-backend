from rest_framework import viewsets
from .models import FinanceApplication, Contact, Vehicle, VehicleDetails
from .serializers import (
    FinanceApplicationSerializer,
    ContactSerializer,
    VehicleDetailsSerializer,
    VehicleSerializer
)


class FinanceApplicationViewSet(viewsets.ModelViewSet):

    queryset = FinanceApplication.objects.all()
    serializer_class = FinanceApplicationSerializer


class ContactViewSet(viewsets.ModelViewSet):

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleDetailsViewSet(viewsets.ModelViewSet):

    queryset = VehicleDetails.objects.all()
    serializer_class = VehicleDetailsSerializer