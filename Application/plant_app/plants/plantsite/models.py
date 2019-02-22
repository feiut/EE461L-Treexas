from django.db import models

# Create your models here.
class Plant(models.Model):
    common_name = models.CharField(max_length=50)
    scientific_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='plants', default ='stateparks')

class StatePark(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='stateparks', default= 'stateparks')


class EcoRegion(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='ecoregions', default ='ecoregions' )


