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

#Hold the data and fields for plants.
class PlantCsv(models.Model):
 #  dbid = models.IntegerField(blank=True, null=True)
    native = models.TextField(db_column='Native', blank=True, null=True)  # Field name made lowercase.
    image = models.TextField(db_column='Image', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    alsoknownas = models.TextField(db_column='AlsoKnownAs', blank=True, null=True)  # Field name made lowercase.
    botanicalname = models.TextField(db_column='BotanicalName', blank=True, null=True)  # Field name made lowercase.
    planttype = models.TextField(db_column='PlantType', blank=True, null=True)  # Field name made lowercase.
    lightrequirement = models.TextField(db_column='LightRequirement', blank=True, null=True)  # Field name made lowercase.
    waterdemand = models.TextField(db_column='WaterDemand', blank=True, null=True)  # Field name made lowercase.
    landscapeuse = models.TextField(db_column='LandscapeUse', blank=True, null=True)  # Field name made lowercase.
    ornamentalvalue = models.TextField(db_column='OrnamentalValue', blank=True, null=True)  # Field name made lowercase.
    native_adapted = models.TextField(db_column='Native/Adapted', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wildlife_alue = models.TextField(db_column='Wildlife alue', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    season = models.TextField(db_column='Season', blank=True, null=True)  # Field name made lowercase.
    deciduous_evergreen = models.TextField(db_column='Deciduous/Evergreen', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    plantform = models.TextField(db_column='PlantForm', blank=True, null=True)  # Field name made lowercase.
    plantspread = models.TextField(db_column='PlantSpread', blank=True, null=True)  # Field name made lowercase.
    plantheight = models.TextField(db_column='PlantHeight', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'plant_csv'

