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



class PlantCsvEcoregions(models.Model):
    dbid = models.IntegerField(blank=True, primary_key=True)
    ecoregion = models.TextField(db_column='Ecoregion', blank=True, null=True)  # Field name made lowercase.
    paragraph = models.TextField(db_column='Paragraph', blank=True, null=True)  # Field name made lowercase.
    trees = models.TextField(db_column='Trees', blank=True, null=True)  # Field name made lowercase.
    shrubs = models.TextField(db_column='Shrubs', blank=True, null=True)  # Field name made lowercase.
    succulents = models.TextField(db_column='Succulents', blank=True, null=True)  # Field name made lowercase.
    vines = models.TextField(db_column='Vines', blank=True, null=True)  # Field name made lowercase.
    vine = models.TextField(db_column='Vine', blank=True, null=True)  # Field name made lowercase.
    conifers = models.TextField(db_column='Conifers', blank=True, null=True)  # Field name made lowercase.
    grasses = models.TextField(db_column='Grasses', blank=True, null=True)  # Field name made lowercase.
    wildflowers = models.TextField(db_column='Wildflowers', blank=True, null=True)  # Field name made lowercase.
    image = models.TextField(db_column='Image', blank=True, null=True)  # Field name made lowercase.
    stateparks = models.TextField(db_column='StateParks', blank=True, null=True)  # Field name made lowercase.
    plants = models.TextField(db_column='Plants', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'plant_csv_ecoregions'





#Hold the data and fields for plants.
class PlantCsv(models.Model):
    #id = models.IntegerField(blank=True, null=True)
    nativeadapted = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    nickname = models.TextField(blank=True, null=True)
    planttype = models.TextField(blank=True, null=True)
    lightreq = models.TextField(blank=True, null=True)
    waterdemand = models.TextField(blank=True, null=True)
    landscapeuse = models.TextField(blank=True, null=True)
    ornamentalvalue = models.TextField(blank=True, null=True)
    wildlifevalue = models.TextField(blank=True, null=True)
    season = models.TextField(blank=True, null=True)
    plantform = models.TextField(blank=True, null=True)
    plantspread = models.TextField(blank=True, null=True)
    plantheight = models.TextField(blank=True, null=True)
    deciduousevergreen = models.TextField(blank=True, null=True)
    soil = models.TextField(blank=True, null=True)
    reproduction = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    sciname = models.TextField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    longi = models.FloatField(blank=True, null=True)
    econregion = models.TextField(blank=True, null=True)
    statepark = models.TextField(blank=True, null=True)
    lifecycle = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'plant_csv'




'''  This might not be needed anymore but saved it just in case
class Stateparks(models.Model): #THIS MODEL NEEDS TO BE CHANGED IT SEEMS TO BE EMPTY
    dbid = models.IntegerField(blank=True, primary_key=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    #region = models.FloatField(db_column='Region', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'stateparks'
'''

class Stateparks(models.Model):
    dbid = models.IntegerField(blank=True, primary_key=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    region = models.TextField(db_column='Region', blank=True, null=True)  # Field name made lowercase.
    image = models.TextField(db_column='Image', blank=True, null=True)  # Field name made lowercase.
    url = models.TextField(db_column='Url', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    plantlist = models.TextField(db_column='PlantList', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'plant_csv_stateparks'

