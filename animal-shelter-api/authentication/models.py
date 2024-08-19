from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.db import models


class CustomUser(AbstractBaseUser):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("inactive", "Inactive"),
    ]
    ROLES_CHOICES = [
        ("adopter", "Adopter"),
        ("volunteer", "Volunteer"),
    ]
    USERNAME_FIELD = "email"

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True, blank=False)
    password = models.CharField(max_length=128)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
    role = models.CharField(max_length=20, choices=ROLES_CHOICES, default="adopter")
    is_superuser = models.BooleanField(
        default=False,
    )

    objects = UserManager()
