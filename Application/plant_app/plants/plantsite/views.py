from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from plantsite.models import Plant
from plantsite.models import PlantCsv
# Create your views here.
'''
Your project’s TEMPLATES setting describes how Django will load and render templates. The default settings file 
configures a DjangoTemplates backend whose APP_DIRS option is set to True. By convention DjangoTemplates looks 
for a “templates” subdirectory in each of the INSTALLED_APPS.

All templates can be referred to with plantsite/<template_name>.html
even though they actually reside in plantsite/templates/plantsite/<template_name>.html'''

class Park(object):

    def __init__(self, name, img, url):
        self.name=name
        self.img = img
        self.url= url

class Ecoregion(object):

    def __init__(self, name, img, url):
        self.name = name
        self.img = img
        self.url = url

class Plant(object):

    def __init__(self, name, img, url):
        self.name = name
        self.img = img
        self.url = url


def page_1(request):
    template = loader.get_template('plantsite/html/mainPage.html')
    return HttpResponse(template.render({}, request))


def state_park_list(request):
    template = loader.get_template('plantsite/html/park_list.html')

    park1 = Park("Pedernales State Park", "sp_pedernales.jpg", "/park1/")
    park2 = Park("Dinosaur Valley State Park", "sp_dinosaur_valley.jpg", "/park2/")
    park3 = Park("Daingerfield State Park", "sp_daingerfield.jpg", "/park3/")
    park4 = Park("Acton State Park", "sp_acton.jpg", "/park4/")
    parklist = [park1, park2, park3, park4]

    context_dict = {"park_list":parklist}
    return HttpResponse(template.render(context_dict, request))

def ecoregion_list(request):
    template = loader.get_template('plantsite/html/eco_list.html')

    eco1 = Ecoregion("Piney Woods", "eco_pineywoods.jpg", "/eco1/")
    eco2 = Ecoregion("Gulf Prairies and Marches", "eco_marshes.jpg", "/eco2/")
    eco3 = Ecoregion("Post Oak Savanah", "eco_postoaksavanah.jpg", "/eco3/")
    eco_list = [eco1, eco2, eco3]

    context_dict = {"ecoregion_list": eco_list}
    return HttpResponse(template.render(context_dict, request))

def pedernales_park(request):
    template = loader.get_template('plantsite/html/park_entry.html')
    park_name = "Pedernales State Park"
    park_description = "Lorem Ipsum Dolor Sit Amut"
    park_img = "sp_pedernales.jpg"

    context_dict = {"park_name":park_name,
                                         "park_description":park_description,
                                         "img_name":park_img}

    return HttpResponse(template.render(context_dict, request))


def dinosaur_valley_park(request):
    template = loader.get_template('plantsite/html/park_entry.html')
    park_name = "Dinosaur Valley State Park"
    park_description = "Lorem Ipsum Dolor Sit Amut"
    park_img = "sp_dinosaur_valley.jpg"

    context_dict = {"park_name":park_name,
                                         "park_description":park_description,
                                         "img_name":park_img}

    return HttpResponse(template.render(context_dict, request))


def daingerfield_park(request):
    template = loader.get_template('plantsite/html/park_entry.html')
    park_name = "Daingerfield State Park"
    park_description = "Lorem Ipsum Dolor Sit Amut"
    park_img = "sp_daingerfield.jpg"

    context_dict = {"park_name":park_name,
                                         "park_description":park_description,
                                         "img_name":park_img}

    return HttpResponse(template.render(context_dict, request))


def acton_park(request):
    template = loader.get_template('plantsite/html/park_entry.html')
    park_name = "Acton State Park"
    park_description = "Lorem Ipsum Dolor Sit Amut"
    park_img = "sp_acton.jpg"

    context_dict = {"park_name":park_name,
                                         "park_description":park_description,
                                         "img_name":park_img}
    return HttpResponse(template.render(context_dict, request))


def piney_eco(request):
    template = loader.get_template('plantsite/html/eco_entry.html')
    name = "Piney Woods"
    description = "Lorem Ipsum Dolor Sit Amut"
    img = "eco_pineywoods.jpg"

    context_dict = {"name": name, "description": description, "img_name": img}
    return HttpResponse(template.render(context_dict, request))


def marshes_eco(request):
    template = loader.get_template('plantsite/html/eco_entry.html')
    name = "Gulf Prairies and Marshes"
    description = "Lorem Ipsum Dolor Sit Amut"
    img = "eco_marshes.jpg"

    context_dict = {"name": name, "description": description, "img_name": img}
    return HttpResponse(template.render(context_dict, request))


def postoaksavanah_eco(request):
    template = loader.get_template('plantsite/html/eco_entry.html')
    name = "Post Oak Savanah"
    description = "Lorem Ipsum Dolor Sit Amut"
    img = "eco_postoaksavanah.jpg"
    context_dict = {"name": name, "description": description, "img_name": img}
    return HttpResponse(template.render(context_dict, request))

def plant_type_list(request):
    template = loader.get_template('plantsite/html/plant_list.html')
    names = PlantCsv.objects.all()
    context_dict = {'plant_names': names}
    return HttpResponse(template.render(context_dict,request))

def plant_profile_view(request):
    template = loader.get_template('plantsite/html/plant_profile.html')
    return HttpResponse(template.render({},request))

#<img src="{{ MEDIA_URL }}{{ image.image.url }}" />
