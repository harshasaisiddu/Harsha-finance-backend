from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet,
    FinanceApplicationViewSet,
    ContactViewSet,
    TagsViewSet,
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

router.register(r'api/category', CategoryViewSet)

router.register(r'api/tags', TagsViewSet)

urlpatterns = router.urls