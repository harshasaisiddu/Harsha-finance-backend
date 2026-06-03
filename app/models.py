from django.db import models
import uuid

# Vehicle Model
class Vehicle(models.Model):

    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Finance Application Model
class FinanceApplication(models.Model):

    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    bike_name = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE
    )
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


# Contact Form Model
class Contact(models.Model):

    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class VehicleDetails(models.Model):

    CATEGORY_CHOICES = [
        ("Scooter", "Scooter"),
        ("Sport Bike", "Sport Bike"),
        ("Premium Bike", "Premium Bike"),
    ]

    vehicle = models.OneToOneField(
        Vehicle,
        on_delete=models.CASCADE,
        related_name="details"
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    image = models.URLField()

    images = models.JSONField(default=list)

    emi = models.CharField(max_length=20)
    emiValue = models.IntegerField()

    downPayment = models.CharField(max_length=20)
    downPaymentValue = models.IntegerField()

    tenure = models.CharField(max_length=50)
    maxTenure = models.IntegerField()

    tag = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    tagColor = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    priceText = models.CharField(max_length=20)

    priceValue = models.IntegerField()

    engineCC = models.CharField(max_length=50)

    mileage = models.CharField(max_length=50)

    description = models.TextField()

    features = models.JSONField(default=list)

    interestRate = models.FloatField(default=9.5)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle.name