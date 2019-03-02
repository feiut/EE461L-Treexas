from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from plantsite.models import Plant
from plantsite.models import PlantCsv
from . import githubdynamic
from .githubdynamic import get_issues_commits

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


def main_page(request):
    template = loader.get_template('plantsite/html/mainPage.html')
    number = request.GET.get('id')
    number = str(number)
    if number.isdigit():
        num = int(number)
        if -1 < num < 30:
            response = redirect('/plant_profile/?id=' + number)
            return response
    return HttpResponse(template.render({}, request))

def about_page(request):
    template = loader.get_template('plantsite/html/about_page.html')

    github_list = get_issues_commits()
    c = [int(k[1]) for k in github_list]
    i = [int(k[2]) for k in github_list]
    context_dict = {"eric_commits": c[2], "eric_issues": i[2], "erick_commits":c[0], "erick_issues":i[0],
                    "connor_commits":c[1], "connor_issues":i[1], "hao_commits":c[3], "hao_issues":i[3],
                    "chaz_commits":c[5], "chaz_issues":c[5], "xiyu_commits":c[6], "xiyu_issues":i[6],
                    "fei_commits":c[4], "fei_issues":i[4], "total_c":sum(c), "total_i":sum(i)}
    return HttpResponse(template.render(context_dict, request))

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
    number = request.GET.get('id')
    prof = PlantCsv.objects.get(id=number)
    context_dict = {'profile': prof}
    return HttpResponse(template.render(context_dict,request))




#<img src="{{ MEDIA_URL }}{{ image.image.url }}" />