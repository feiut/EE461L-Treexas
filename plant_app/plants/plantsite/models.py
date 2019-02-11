from django.db import models

# Create your models here.
class Plant(models.Model):
    common_name = models.CharField(max_length=50)
    scientific_name = models.CharField(max_length=50)

class StatePark(models.Model):
    name = models.CharField(max_length=50)

class EcoRegion(models.Model):
    name = models.CharField(max_length=50)