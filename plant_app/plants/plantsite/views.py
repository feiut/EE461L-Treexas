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
    template = loader.get_template('plantsite/page_1.html')
    return HttpResponse(template.render({}, request))


def page_2(request):
    template = loader.get_template('plantsite/page_2.html')
    return HttpResponse(template.render({}, request))


def page_3(request):
    template = loader.get_template('plantsite/page_3.html')
    return HttpResponse(template.render({}, request))


def page_4(request):
    template = loader.get_template('plantsite/page_4.html')
    return HttpResponse(template.render({}, request))


def page_5(request):
    template = loader.get_template('plantsite/page_5.html')
    return HttpResponse(template.render({}, request))


def page_6(request):
    template = loader.get_template('plantsite/page_6.html')
    return HttpResponse(template.render({}, request))

