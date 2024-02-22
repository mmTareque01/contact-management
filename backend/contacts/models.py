import uuid
from django.db import models
from django.utils import timezone


class Address(models.Model):
    addressId = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    zipCode = models.CharField(max_length=20, blank=True, null=True)
    others = models.TextField(blank=True, null=True)


class Contact(models.Model):
    CId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phoneNumber = models.CharField(max_length=15, blank=True, null=True)

    # Reference to the Address model
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, blank=True, null=True)

    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)
    isDeleted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.updatedAt = timezone.now()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.isDeleted = True
        self.save()

    def __str__(self):
        return f"{self.name} ({self.email})"
