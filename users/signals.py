from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, DriverProfile, ClientProfile, ManagerProfile

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == CustomUser.Role.DRIVER:
            DriverProfile.objects.create(user=instance)
        elif instance.role == CustomUser.Role.CLIENT:
            ClientProfile.objects.create(user=instance)
        elif instance.role == CustomUser.Role.MANAGER:
            ManagerProfile.objects.create(user=instance)