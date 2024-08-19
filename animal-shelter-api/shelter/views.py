from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from authentication.models import CustomUser
from authentication.serializers import CustomUserSerializer
from .models import Adoption, Animal
from .serializers import AdoptionSerializer, AnimalSerializer
from authentication.permissions import IsAdmin, IsAdopter, IsVolunteer


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "destroy"]:
            self.permission_classes = [IsAdmin | IsVolunteer]
        else:
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()


class AdopterViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.filter(role="adopter")
    serializer_class = CustomUserSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "destroy"]:
            self.permission_classes = [IsAdmin]
        else:
            self.permission_classes = [IsAdmin | IsVolunteer]
        return super().get_permissions()


class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.filter(role="volunteer")
    serializer_class = CustomUserSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "destroy"]:
            self.permission_classes = [IsAdmin]
        else:
            self.permission_classes = [IsAdmin | IsVolunteer]
        return super().get_permissions()


class AdoptionViewSet(viewsets.ModelViewSet):
    queryset = Adoption.objects.all()
    serializer_class = AdoptionSerializer

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [IsAdmin | IsAdopter]
        elif self.action in ["update", "destroy"]:
            self.permission_classes = [IsAdmin | IsVolunteer]

        return super().get_permissions()

    def get_queryset(self):
        user = self.request.user

        # Si el usuario es un adoptante, solo puede ver sus propias adopciones
        if user.role == "adopter":
            return Adoption.objects.filter(adopter=user)

        # Si es un administrador o voluntario, pueden ver todas las adopciones
        elif user.role in ["admin", "volunteer"]:
            return Adoption.objects.all()

        # En caso de que haya otros roles o usuarios no autenticados
        raise PermissionDenied("You do not have permission to perform this action.")
