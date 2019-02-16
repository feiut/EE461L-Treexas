from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
'''
Your project’s TEMPLATES setting describes how Django will load and render templates. The default settings file 
configures a DjangoTemplates backend whose APP_DIRS option is set to True. By convention DjangoTemplates looks 
for a “templates” subdirectory in each of the INSTALLED_APPS.

All templates can be referred to with plantsite/<template_name>.html
even though they actually reside in plantsite/templates/plantsite/<template_name>.html'''


def page_1(request):
    template = loader.get_template('plantsite/html/page_1.html')
    return HttpResponse(template.render({}, request))


def state_park_list(request):
    template = loader.get_template('plantsite/html/park_list.html')
    return HttpResponse(template.render({}, request))


def pedernales_park(request):
    template = loader.get_template('plantsite/html/park_entry.html')
    park_name = "Pedernales State Park"
    park_description = "Lorem Ipsum Dolor Sit Amut"
    park_img = "sp_pedernales.jpg"

    return HttpResponse(template.render({"park_name":park_name,
                                         "park_description":park_description,
                                         "img_name":park_img}, request))


def dinosaur_valley_park(request):
    template = loader.get_template('plantsite/html/park_entry.html')
    park_name = "Dinosaur Valley State Park"
    park_description = "Lorem Ipsum Dolor Sit Amut"
    park_img = "sp_dinosaur_valley.jpg"

    return HttpResponse(template.render({"park_name":park_name,
                                         "park_description":park_description,
                                         "img_name":park_img}, request))


def daingerfield_park(request):
    template = loader.get_template('plantsite/html/park_entry.html')
    park_name = "Daingerfield State Park"
    park_description = "Lorem Ipsum Dolor Sit Amut"
    park_img = "sp_daingerfield.jpg"

    return HttpResponse(template.render({"park_name":park_name,
                                         "park_description":park_description,
                                         "img_name":park_img}, request))

