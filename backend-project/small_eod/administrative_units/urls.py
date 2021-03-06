from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import AdministrativeUnitViewSet

router = SimpleRouter()
router.register(
    "administrative_units",
    AdministrativeUnitViewSet,
    basename="administrative_unit",
)

urlpatterns = [
    path("", include(router.urls)),
]
