from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        CLIENT = 'CLIENT', 'Client'
        DRIVER = 'DRIVER', 'Driver'
        MANAGER = 'MANAGER', 'Manager'
        ADMIN = 'ADMIN', 'Admin'

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.CLIENT)
    phone_number = models.CharField(max_length=20, blank=True)

    @property
    def id_driver(self):
        return self.role == self.Role.DRIVER
    
    @property
    def is_client(self):
        return self.role == self.Role.CLIENT
    
    @property
    def is_manager(self):
        return self.role == self.Role.MANAGER

class DriverProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="driver_profile"
    )

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_drivers",
    )

    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_drivers",
    )

class ClientProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='client_profile'
    )

class ManagerProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='manager_profile'
    )
    
    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="managed_warehouse",
    )