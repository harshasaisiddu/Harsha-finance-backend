from rest_framework import viewsets, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Tags, Vehicle, VehicleDetails, FinanceApplication, Contact
from .serializers import (
    CategorySerializer,
    TagsSerializer,
    VehicleSerializer,
    VehicleDetailsSerializer,
    FinanceApplicationSerializer,
    ContactSerializer,
)


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all().order_by("-created_at")
    serializer_class = VehicleSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "brand"]
    ordering_fields = ["created_at", "name", "price"]


class VehicleDetailsViewSet(viewsets.ModelViewSet):
    queryset = VehicleDetails.objects.select_related("vehicle").all()
    serializer_class = VehicleDetailsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["vehicle", "category"]
    search_fields = ["vehicle__name", "category"]


class FinanceApplicationViewSet(viewsets.ModelViewSet):
    queryset = FinanceApplication.objects.select_related("bike_name").order_by("-created_at")
    serializer_class = FinanceApplicationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["status"]
    search_fields = ["full_name", "phone", "city"]
    ordering_fields = ["created_at", "status"]


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.select_related("vehicle").order_by("-created_at")
    serializer_class = ContactSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["full_name", "phone"]
    ordering_fields = ["created_at"]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer