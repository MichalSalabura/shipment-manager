from django.db import models

class Vehicle(models.Model):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    registration = models.CharField(max_length=20, unique=True)
    available_space = models.FloatField()
    mileage = models.FloatField()
    last_serviced = models.DateField(null=True, blank=True)
    service_due = models.DateField(null=True, blank=True)

class Warehouse(models.Model):
    code = models.CharField(max_length=20, unique=True)
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50, blank=True)
    address_city = models.CharField(max_length=50)
    address_region = models.CharField(max_length=50)
    address_post_code = models.CharField(max_length=50)
    country = models.CharField(max_length=50)