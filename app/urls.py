from rest_framework.routers import DefaultRouter
from .views import (
    FinanceApplicationViewSet,
    ContactViewSet,
    VehicleViewSet
)

router = DefaultRouter()

router.register(
    r'apply-finance',
    FinanceApplicationViewSet
)

router.register(
    r'contact-form',
    ContactViewSet
)

router.register(r'vehicles', VehicleViewSet)

urlpatterns = router.urls