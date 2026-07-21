from django.db import models
from django.contrib.auth.models import User

class Package(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_package")
    driver_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="assigned_package")
    from_name = models.CharField(max_length=50)
    from_address_line_1 = models.CharField(max_length=50)
    from_address_line_2 = models.CharField(max_length=50, blank=True)
    from_address_city = models.CharField(max_length=50)
    from_address_region = models.CharField(max_length=50)
    from_address_post_code = models.CharField(max_length=50)
    from_country = models.CharField(max_length=50)
    
    to_name = models.CharField(max_length=50)
    to_address_line_1 = models.CharField(max_length=50)
    to_address_line_2 = models.CharField(max_length=50, blank=True)
    to_address_city = models.CharField(max_length=50)
    to_address_region = models.CharField(max_length=50)
    to_address_post_code = models.CharField(50)
    to_country = models.CharField(50)
    receipient_phone = models.CharField(max_length=50)
    receipent_email = models.CharField(max_length=50)
    scheduled_delivery = models.DateTimeField()
    
    width = models.FloatField()
    height = models.FloatField()
    depth = models.FloatField()