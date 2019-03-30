from django.test import TestCase
from django.test.client import Client
from plantsite.models import PlantCsv
#from plantsite.models import Plant
#from plantsite.models import StatePark
#from plantsite.models import EcoRegion
from plantsite.models import PlantCsvEcoregions
from plantsite.models import Stateparks
from plantsite.views import search_plants_with_string
from plantsite.views import get_all_plants
from plantsite.views import get_park_with_dbid
from plantsite.views import get_all_parks
from plantsite.views import search_park_with_string


# Create your tests here.

class viewTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

        
        PlantCsv.objects.create(name="Plant1")
        
        PlantCsvEcoregions.objects.create(dbid=0, ecoregion="Eco1", paragraph="Null", trees="", shrubs="",
                                          succulents="", vines="", vine="", conifers="", grasses="", wildflowers="", image="https/test_img.png")
                                          
        Stateparks.objects.create(dbid=0, name="Park1", latitude="32.24", longitude="-99.87")
        
        # Park.objects.create("Park2", "sp_dinosaur_valley.jpg", "/park2/")
        # Park.objects.create("Park3", "sp_daingerfield.jpg", "/park3/")
        # Park.objects.create("Park4", "sp_acton.jpg", "/park4/")
        # Ecoregion.objects.create("Eco1", "eco_pineywoods.jpg", "/eco1/")
        # Ecoregion.objects.create("Eco2", "eco_marshes.jpg", "/eco2/")
        # Ecoregion.objects.create("Eco3", "eco_postoaksavanah.jpg", "/eco3/")
        # Plant.objects.create("Plant1", "eco_pineywoods.jpg", "/plant1/")
        # Plant.objects.create("Plant2", "eco_pineywoods.jpg", "/plant2/")
        # Plant.objects.create("Plant3", "eco_pineywoods.jpg", "/plant3/")

    # def test_search_plants_with_string(self):
    #     leftover = search_plants_with_string("1")
    #     self.assertEqual(leftover.name, "Plant1")

    # def search_plants_with_string(p):
    #     results = PlantCsv.objects.all()
    #     leftover = set()
    #     for plants in results:
    #         if (p.lower() in plants.alsoknownas.lower()) or (p.lower() in plants.botanicalname.lower()) or (
    #                 p.lower() in plants.name.lower()):
    #             leftover.add(plants)
    #     return leftover

    # def test_get_all_plants(self):
    #     results = get_all_plants()
    #     self.assertEqual(len(PlantCsv.objects.all()), len(results))

    # def get_all_plants():
    #     results = PlantCsv.objects.all()
    #     return results

    # def test_search_park_with_string(self):
    #     leftover = search_park_with_string("k3")
    #     self.assertEqual(leftover.name, "Park3")

    # def search_park_with_string(p):
    #     qset = Stateparks.objects.all()
    #     leftover = set()
    #     for parks in qset:
    #         if (p.lower() in parks.name.lower()):
    #             leftover.add(parks)
    #     return leftover

    def test_main_page(self): #Passed
        # Issue a GET request.
        response = self.client.get('')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_about_page(self): #Passed
        # Issue a GET request.
        response = self.client.get('/about/')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_park_list_view(self):
        # Issue a GET request.
        response = self.client.post('/park_list/', {})
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_park_profile(self):
        # Issue a GET request.
        response = self.client.get('/park_profile/?id=0')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_plant_type_list(self): #Passed
        # Issue a GET request.
        response = self.client.get('/plant_list/')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    
    def test_ecoregion_list(self): #Passed
        # Issue a GET request.
        response = self.client.get('/eco_list/')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
    
    
    def test_eco_profile_view(self):
        # Issue a GET request.
        response = self.client.get('/eco_profile/?id=0')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)


    def test_get_all_plants(self):
        result = get_all_plants()
        self.assertEqual(len(result), PlantCsv.objects.count())

    # def test_get_plant_with_id(self):
    #     result = get_plant_with_id(0)
    #     self.assertEqual(result.id, 0)

    def test_search_plants_with_string(self):
        leftover = search_plants_with_string("1")
        self.assertEqual(leftover.name, "Plant1")

    def test_search_park_with_string(self):
        leftover = search_park_with_string("1")
        self.assertEqual(leftover.name, "Park1")

    def test_get_park_with_dbid(self):
        result = get_park_with_dbid(0)
        self.assertEqual(result.name, "Park1")

    def test_get_all_parks(self):
        result = get_all_parks()
        self.assertEqual(len(result), Stateparks.objects.count())

