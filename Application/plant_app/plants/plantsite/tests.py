from django.test import TestCase
from django.test.client import Client
from plantsite.models import PlantCsv
from plantsite.models import PlantCsvEcoregions
from plantsite.models import Stateparks
from plantsite.views import search_plants_with_string
from plantsite.views import get_all_plants
from plantsite.views import get_park_with_dbid
from plantsite.views import get_all_parks
from plantsite.views import search_park_with_string
from plantsite.views import is_number
from plantsite.views import empty_check
from plantsite.views import plants_each
from plantsite.views import plant_profile_view
from plantsite.views import eco_profile_view
from plantsite.views import park_profile_view
from plantsite.views import get_plant_with_id
from plantsite.views import filter_plants_with_parameters

# Create your tests here.

class viewTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

        # Tests must use fake dataset to do the works
        
        #PlantCsv.objects.create(name="Plant1", lat="32.24", longi="-99.87", image="test", nickname="test")
        PlantCsv.objects.create(id=1, name="Plant1", lat="32.24", image="test", nickname="test", planttype=" test", waterdemand=" Low", plantform=" Bushy", season=" Spring", nativeadapted=" Native", lightreq=" Full Sun", edibility="toxic", endangered="N/A", ecoregionids="[1]", statepark="[1]", search_times="1")
        PlantCsv.objects.create(id=2, name="Plant2", lat="32.24", image="test", nickname="test", planttype=" Shrub", waterdemand=" test", plantform=" Bushy", season=" Spring", nativeadapted=" Native", lightreq=" Full Sun", edibility="toxic", endangered="N/A", ecoregionids="[1]", statepark="[1]", search_times="1")
        PlantCsv.objects.create(id=3, name="Plant3", lat="32.24", image="test", nickname="test", planttype=" Shrub", waterdemand=" Low", plantform=" test", season=" Spring", nativeadapted=" Native", lightreq=" Full Sun", edibility="toxic", endangered="N/A", ecoregionids="[1]", statepark="[1]", search_times="1")
        PlantCsv.objects.create(id=4, name="Plant4", lat="32.24", image="test", nickname="test", planttype=" Shrub", waterdemand=" Low", plantform=" Bushy", season=" test", nativeadapted=" Native", lightreq=" Full Sun", edibility="toxic", endangered="N/A", ecoregionids="[1]", statepark="[1]", search_times="1")
        PlantCsv.objects.create(id=5, name="Plant5", lat="32.24", image="test", nickname="test", planttype=" Shrub", waterdemand=" Low", plantform=" Bushy", season=" Spring", nativeadapted=" test", lightreq=" Full Sun", edibility="toxic", endangered="N/A", ecoregionids="[1]", statepark="[1]", search_times="1")
        PlantCsv.objects.create(id=6, name="Plant6", lat="32.24", image="test", nickname="test", planttype=" Shrub", waterdemand=" Low", plantform=" Bushy", season=" Spring", nativeadapted=" Native", lightreq=" test", edibility="toxic", endangered="N/A", ecoregionids="[1]", statepark="[1]", search_times="1")
        PlantCsv.objects.create(id=7, name="Plant7", lat="32.24", image="test", nickname="test", planttype=" Shrub", waterdemand=" Low", plantform=" Bushy", season=" Spring", nativeadapted=" Native", lightreq=" Full Sun", edibility="test", endangered="N/A", ecoregionids="[1]", statepark="[1]", search_times="1")
        PlantCsv.objects.create(id=8, name="Plant8", lat="32.24", image="test", nickname="test", planttype=" Shrub", waterdemand=" Low", plantform=" Bushy", season=" Spring", nativeadapted=" Native", lightreq=" Full Sun", edibility="toxic", endangered="Endangered", ecoregionids="[1]", statepark="[1]", search_times="1")

        PlantCsvEcoregions.objects.create(id=1, ecoregion="Eco1", paragraph="Null", trees="Null", shrubs="Null",
                                          succulents="Null", vines="Null", vine="Null", conifers="Null", grasses="Null", wildflowers="Null", image="https/test_img.png", stateparks="[1]", plants="[1]")
                                          
        Stateparks.objects.create(id=1, name="Park1", latitude="32.24", longitude="-99.87", plantlist="[1]", ecoregionlist="[1]", image="test")
        
        # Park.objects.create("Park2", "sp_dinosaur_valley.jpg", "/park2/")
        # Park.objects.create("Park3", "sp_daingerfield.jpg", "/park3/")
        # Park.objects.create("Park4", "sp_acton.jpg", "/park4/")

        # Ecoregion.objects.create("Eco1", "eco_pineywoods.jpg", "/eco1/")
        # Ecoregion.objects.create("Eco2", "eco_marshes.jpg", "/eco2/")
        # Ecoregion.objects.create("Eco3", "eco_postoaksavanah.jpg", "/eco3/")

        # Plant.objects.create("Plant1", "eco_pineywoods.jpg", "/plant1/")
        # Plant.objects.create("Plant2", "eco_pineywoods.jpg", "/plant2/")
        # Plant.objects.create("Plant3", "eco_pineywoods.jpg", "/plant3/")

    '''Test the urls and the webpage framework'''
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

    def test_park_list_view(self): #Passed finally
        # Issue a GET request.
        response = self.client.post('/park_list/', {})
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

    #def test_plants_each(self): #Passed
        # Issue a GET request.
        #response = self.client.get('/plant_profile/?id=1')
        # Check that the response is 200 OK.
        #self.assertEqual(response.status_code, 200)

    def test_plant_profile_view(self): #Passed
        # Issue a GET request.
        response = self.client.get('/plant_profile/?id=1')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_eco_profile_view(self): #Passed
        # Issue a GET request.
        response = self.client.get('/eco_profile/?id=1')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_park_profile_view(self): #Passed
        # Issue a GET request.
        response = self.client.get('/park_profile/?id=1')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    '''Test the inner functions corresponding to searching in views.py'''

    def test_get_all_plants(self):#Passed
        result = get_all_plants()
        self.assertEqual(len(result), PlantCsv.objects.count())

    def test_get_plant_with_id(self): #Passed finally finally finally T_T
        result = get_plant_with_id(1)
        self.assertEqual(result.id, 1)

    def test_search_plants_with_string(self):#Passed
        leftover = search_plants_with_string("1")
        self.assertEqual(list(leftover)[0].name, "Plant1")

    def test_search_park_with_string(self):#Passed
        leftover = search_park_with_string("1")
        self.assertEqual(list(leftover)[0].name, "Park1")

    def test_get_park_with_dbid(self): #Passed
        result = get_park_with_dbid(1)
        self.assertEqual(result.name, "Park1")

    def test_get_all_parks(self):#Passed
        result = get_all_parks()
        self.assertEqual(len(result), Stateparks.objects.count())

    def test_is_number(self):#Passed
        s = 123
        self.assertEqual(is_number(s), True)

    def test_is_not_number(self):#Passed
        s = "abrakadabra"
        self.assertEqual(is_number(s), False)

    def test_empty_check(self):#Passed
        item = ""
        self.assertEqual(empty_check(item), "true")

    def test_not_empty_check(self):#Passed
        item = "flower"
        self.assertEqual(empty_check(item), "false")

    '''Test the very important filter in different branches and main pathes.'''
    def test_filter_plants_with_parameters1(self):
        names = filter_plants_with_parameters("test", "AllType", "AllType", "AllType", "AllType", "AllType", "AllType", "AllType")
        self.assertEqual(list(names)[0].id, 1)

    def test_filter_plants_with_parameters2(self):
        names = filter_plants_with_parameters("AllType", "test", "AllType", "AllType", "AllType", "AllType", "AllType", "AllType")
        self.assertEqual(list(names)[0].id, 2)

    def test_filter_plants_with_parameters3(self):
        names = filter_plants_with_parameters("AllType", "AllType", "test", "AllType", "AllType", "AllType", "AllType", "AllType")
        self.assertEqual(list(names)[0].id, 3)

    def test_filter_plants_with_parameters4(self):
        names = filter_plants_with_parameters("AllType", "AllType", "AllType", "test", "AllType", "AllType", "AllType", "AllType")
        self.assertEqual(list(names)[0].id, 4)

    def test_filter_plants_with_parameters5(self):
        names = filter_plants_with_parameters("AllType", "AllType", "AllType", "AllType", "test", "AllType", "AllType", "AllType")
        self.assertEqual(list(names)[0].id, 5)

    def test_filter_plants_with_parameters6(self):
        names = filter_plants_with_parameters("AllType", "AllType", "AllType", "AllType", "AllType", "test", "AllType", "AllType")
        self.assertEqual(list(names)[0].id, 6)

    def test_filter_plants_with_parameters7(self):
        names = filter_plants_with_parameters("AllType", "AllType", "AllType", "AllType", "AllType", "AllType", "test", "AllType")
        self.assertEqual(list(names)[0].id, 7)

    def test_filter_plants_with_parameters8(self):
        names = filter_plants_with_parameters("AllType", "AllType", "AllType", "AllType", "AllType", "AllType", "AllType", "test")
        self.assertEqual(list(names)[0].id, 8)

    def test_filter_plants_with_parameters_all(self):
        names = filter_plants_with_parameters("AllType", "AllType", "AllType", "AllType", "AllType", "AllType", "AllType", "AllType")
        self.assertEqual(len(names), 8)

    def test_filter_plants_with_parameters_none(self):
        names = filter_plants_with_parameters("test", "test", "AllType", "AllType", "AllType", "AllType", "AllType", "AllType")
        self.assertEqual(len(names), 0)