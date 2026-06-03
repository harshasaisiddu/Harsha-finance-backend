from django.contrib import admin
from .models import Vehicle, FinanceApplication, Contact, VehicleDetails


admin.site.register(Vehicle)
admin.site.register(FinanceApplication)
admin.site.register(Contact)
admin.site.register(VehicleDetails)