from rest_framework import viewsets
from .models import FinanceApplication, Contact
from .serializers import (
    FinanceApplicationSerializer,
    ContactSerializer
)


class FinanceApplicationViewSet(viewsets.ModelViewSet):

    queryset = FinanceApplication.objects.all()
    serializer_class = FinanceApplicationSerializer


class ContactViewSet(viewsets.ModelViewSet):

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer