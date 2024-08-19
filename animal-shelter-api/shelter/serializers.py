from rest_framework import serializers
from .models import Adoption, Animal


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = "__all__"


class AdoptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adoption
        fields = [
            "animal",
            "adopter",
            "volunteer",
            "status",
        ]

    def create(self, validated_data):
        # Set the adopter to the current user
        validated_data["adopter"] = self.context["request"].user
        animal = validated_data["animal"]

        # Check if the animal is available
        if animal.status != "available":
            raise serializers.ValidationError(
                "This animal is not available for adoption"
            )

        # Set the animal status to pending
        animal.status = "pending"
        animal.save()

        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Check if the status is being changed to finished
        if validated_data.get("status") == "finished":
            instance.animal.status = "adopted"
            instance.animal.save()

        return super().update(instance, validated_data)
