from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from .serializers import RegisterSerializer, CustomUserSerializer
from .models import CustomUser


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_object(self):
        # Obtenemos el objeto del usuario que se intenta acceder
        obj = super().get_object()

        # Verificamos si el usuario es el mismo o un administrador
        if self.request.user == obj or self.request.user.is_superuser:
            return obj
        else:
            raise PermissionDenied("You do not have permission to perform this action.")
