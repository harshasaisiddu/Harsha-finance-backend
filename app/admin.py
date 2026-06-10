from django.contrib import admin
from .models import Category, Vehicle, FinanceApplication, Contact, VehicleDetails, Tags


admin.site.register(Vehicle)
admin.site.register(FinanceApplication)
admin.site.register(Contact)
admin.site.register(VehicleDetails)
admin.site.register(Category)
admin.site.register(Tags)