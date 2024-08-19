from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdopterViewSet, AdoptionViewSet, AnimalViewSet, VolunteerViewSet

router = DefaultRouter()
router.register(r"animals", AnimalViewSet)
router.register(r"adopters", AdopterViewSet, basename="adopter")
router.register(r"volunteers", VolunteerViewSet, basename="volunteer")
router.register(r"adoptions", AdoptionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
