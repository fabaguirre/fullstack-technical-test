from django.db import models


class Animal(models.Model):
    TYPE_CHOICES = [
        ("dog", "Dog"),
        ("cat", "Cat"),
    ]

    STATUS_CHOICES = [
        ("adopted", "Adopted"),
        ("available", "Available for adoption"),
        ("pending", "Pending adoption"),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="available"
    )

    def __str__(self):
        return self.name


class Adoption(models.Model):
    STATUS_CHOICES = [
        ("finished", "Finished"),
        ("in_progress", "In progress"),
        ("requested", "Requested"),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    adopter = models.ForeignKey(
        "authentication.CustomUser",
        on_delete=models.CASCADE,
        related_name="adopter",
        default=None,
    )
    volunteer = models.ForeignKey(
        "authentication.CustomUser", on_delete=models.CASCADE, related_name="volunteer"
    )
    status = models.CharField(
        max_length=11, choices=STATUS_CHOICES, default="requested"
    )
