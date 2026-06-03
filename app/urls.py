from rest_framework.routers import DefaultRouter
from .views import (
    FinanceApplicationViewSet,
    ContactViewSet,
    VehicleDetailsViewSet,
    VehicleViewSet
)

router = DefaultRouter()

router.register(
    r'api/apply-finance',
    FinanceApplicationViewSet
)

router.register(
    r'api/contact-form',
    ContactViewSet
)

router.register(r'api/vehicles', VehicleViewSet)

router.register(r'api/vehicle-details', VehicleDetailsViewSet)

urlpatterns = router.urls