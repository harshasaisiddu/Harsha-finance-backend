from django.db import models


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