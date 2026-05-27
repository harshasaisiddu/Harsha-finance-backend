from rest_framework.routers import DefaultRouter
from .views import (
    FinanceApplicationViewSet,
    ContactViewSet
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

urlpatterns = router.urls