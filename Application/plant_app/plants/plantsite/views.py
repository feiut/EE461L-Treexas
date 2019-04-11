from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from plantsite.models import Plant
from plantsite.models import PlantCsv
from plantsite.models import PlantCsvEcoregions
from plantsite.models import Stateparks
from . import githubdynamic
from .githubdynamic import get_issues_commits
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import re
# Create your views here.
'''
Your project’s TEMPLATES setting describes how Django will load and render templates. The default settings file
configures a DjangoTemplates backend whose APP_DIRS option is set to True. By convention DjangoTemplates looks
for a “templates” subdirectory in each of the INSTALLED_APPS.

All templates can be referred to with plantsite/<template_name>.html
even though they actually reside in plantsite/templates/plantsite/<template_name>.html'''

''' Some important functions that are useful '''
def search_plants_with_string(p):
    result = PlantCsv.objects.all()
    leftover = set()
    for plants in result:
        if (p.lower() in plants.nickname.lower()) or (p.lower() in plants.name.lower()):
            if ('none' in plants.image.lower()) or ("n/a" in plants.image.lower()):
                plants.image ='data:image/jpeg;base64,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'
            leftover.add(plants)
    return leftover


def filter_plants_with_parameters(value_1, value_2, value_3, value_4, value_5, value_6):
    if not value_1:
        names = PlantCsv.objects.all()
    elif str(value_1) == "AllType":
        names = PlantCsv.objects.all()
    else:
        names = PlantCsv.objects.filter(planttype__contains=str(value_1))
    if not value_2:
        names = names.all()
    elif str(value_2) == "AllType":
        names = names.all()
    else:
        names = names.filter(waterdemand__contains=str(value_2))
    if not value_3:
        names = names.all()
    elif str(value_3) == "AllType":
        names = names.all()
    else:
        names = names.filter(plantform__contains=str(value_3))
    if not value_4:
        names = names.all()
    elif str(value_4) == "AllType":
        names = names.all()
    else:
        names = names.filter(season__contains=str(value_4))
    if not value_5:
        names = names.all()
    elif str(value_5) == "AllType":
        names = names.all()
    else:
        names = names.filter(nativeadapted__contains=str(value_5))
    if not value_6:
        names = names.all()
    elif str(value_6) == "AllType":
        names = names.all()
    else:
        names = names.filter(lightreq__contains=str(value_6))
    return names


def fix_plant_defualt(qset):
    for plants in qset:
        if ('none' in plants.image.lower()) or ("n/a" in plants.image.lower()):
            plants.image ='data:image/jpeg;base64,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'
    return qset



def get_all_plants():
    results =  PlantCsv.objects.all()
    for plant in results:
    	if ('none' in plant.image.lower()) or ("n/a" in plant.image.lower()):
                plant.image ='data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxISEhITERISEhUWEhUQEBUSFxIYFhAQFxgYFxUSFhcYHSggGRolHRUVIjEhJSktMi4uFx8zODMsNygtLisBCgoKDg0OGxAQGy0mICAtLS8vMCstLTAvLis3NTctLS0rLS0vMC0tLTYtKy0vLS0tLS0tLS0vLTU1LSstLS0tNf/AABEIALcBEwMBIgACEQEDEQH/xAAcAAEAAQUBAQAAAAAAAAAAAAAABwIDBAUGAQj/xAA6EAACAQIEAwYEBQMCBwAAAAAAAQIDEQQSITEFBkETIlFhcYEykaGxB0Jy0eEjUvAz8RQVF0NiksH/xAAaAQEAAwEBAQAAAAAAAAAAAAAAAQIEAwUG/8QAMBEBAAIBAgUBBgQHAAAAAAAAAAECEQMSBAUhMUETIlFxkbHBMkJhoRQzNGKB0fH/2gAMAwEAAhEDEQA/AJxAAAAAAAAAAAAAAAAAAAAACmpNRTlJ2STbb6JatlRy3O/FskOwj8U13/KHh7nDideuhpzefH1JYVHmyfauW9Nyccul0ls0/Gx2NDEwmk4yTurqzWzIjgrx32lb6fwZ+AxEqcoyi7NO/wDB8zw3N9TRmfU9qJn5fD/TnFkpAx8DiVVpxmuq18n1RkH1dbRasWjtLoAAsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADD4rxCFCm5z9IrrKXRIjDieJlWqSqSesnfTp0S9LJfI6TnvEy7SENlGOZebe7+hx85fyvD+D5XmvE21NadOO1fqpaV+EbU73Xx6ey6/MqhUsr7/sURS7OF9ryfq9EKfedvOzZ48w5WnEu75Hc3Tm2rQzd3xcutvLY6Ys4PDxpwjCKsopJfuXj7nhND0dGunns7xGIAAaUgAAAAAAAAAAAAAAAAAAAAAAAABbrQk/hllfomn6r9miJnEC4DVYjEYqH/AGqdVeMG0/k7mmx3MWIWjgqXs831/Yxa3MNPRj2ot8p/5+464oqVYx1k0vVnAVePVWrOcvn+xh1OKN7t+55upz2PyUn/ACjdDv3xejeyk36JnsOK0m0r2vtcjqXEPDV9CulxO6v9UzNHOeJz+GE5qk9M9ON4RzC1JJyzR0uuqX9yOxjJNJrVPVeaPd4TjKcTWcdJjvA5L8QcHeFOql8LcJfpeqfzT+ZwNSd/XxJlxlCNSEozScWtb/ciLEYZwrOk/wAs3Dz3PF5vobNb1I/N9VLQu4iGlNP+xX876m+5P4P2s884t046q+0pdF5mOuGdpUeeWSEXZbXaWml9tjqocYpUYRhC1oqyS10/z7mLgqaW7frT0jx71fT9rMt+DS4DiVSvK0IqMV8UrfReZuj63Q1661d1YnH6uoADsAAAAAAAAAAAAAAAAAAAAAAAAAAAFNSmpK0kpLwaTX1KgJjI11XgeHlvSj7XX2MCtyhh5f3r32OgBnvwmjf8VI+Q4+vyQm+7V/8AaOvzTMGvyVWjd0505eTur+WqO+Bntyzh57RhGIRtLlfFQ1VPVeEou/1udbyxiKmTsq0XGUV3c2l4+Hsbwt1qSktdPBrdPxRXR5fHD336cz8Jx1TEQt4+plpzfkR5jsTN1JOS797S018F9kdji+Mwp5qeI0kkmvCrFu2aPn5FHBoxq1KldxWrtG62itI/RGPjqRxWrWlbdZ8e7vmZ/ZP6OWw/C69SXdpya6t6L5s33DOVbWdeSejWWG1n0bOoBp0OUaGnObdUKKNKMUoxSiloktkVgHqRERGIAAEgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA0XNvD4VKSm43lTd4/pekl9n7GVy9Ty0VpZPVelv9y9xn/QqfpZXwv8A0qf6V9jzPSj+P3f2ffBjyygAemAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB42enjV99QMDi2Jp9lUTnBdx/mRY5e4lSqU4whNSlGPeSUu76u1jPxVGPZzWVfDLovAweWKDhQV2nd30VjDaJjiqz76z9YW67W2ABuVAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbxPwS/S/sYfA3/Rj6GbX+GX6X9jA4A/6UTLf+or8J+zrH8ufjDZAA1OQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFM5pK7aS8XoBUeNnLcc/EHh+Fsp1s7baSpLPs0parRWuupwPNn4surTlDCRhCMr05SqXlKUGmnZbK/uUm8QvXTmUsYji1BPJ2sHOWeEYppvNGN5J22srb+K8Szy1O9FerPlqNXvpuo3KU03bwWy3+nkd1/1ArU6LgppQzKLULxqK6Wa8r2cdzJe1vWrbHSIn7O9dP2JjL6BB87rmbFxcXRxc3BO6Sbi1dWs73vsl4FfD+fsfQ7RVKspZr2dVJuLS3XTbwO8a8T4Vnh5jy+hQRn+HnOU6+IdHEVrtwy0lZOLlFJtZlrm39STDrS8WjMOV6TScSAAsoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABhca4nDDUKlep8MIuTWl5NbRV+rAr4lxGlh6cqtecacIq8pSeiII/EP8VHjI9hhYunSzNzlO16yT7unRaJ29DlOb+cMTj6jlUnJQzSdOlfu00+i8fVnOU7X19znM5dYjDJqVFO19HffyLMLttJN2u35JfmKo10o933Xj4O/gVxqx7skla1nG2ubXr1s+pTsv3UxulLLaTVoq+jTu9Vf0PZVJJ5U7yer1T13t7FipUaabSd23fxW1i9hsRmzXSvKyjKyupbXYmCJ64dBg605wkrtVNMitZuWifktkewxDmqmd2kk5LbVrRv1crqxTg8M1Ti4ty7/AHtHeFS1mm3o1otN9DBhiE5tSese7Nx/Mlomr7PVaeRnxmZw05xEZb3hOIlCpF0pZJ5r3z2ytax1vo9Htpojv+Cc/wCIpNRrPtYRl3m1ec7q2VS9dfoRLg6sllUpXWZwUYZc00ldON1onsbeNaUnJJNPK5U7699WaWm70shO6s9JI23jrD6Cp834KUaclXjae291+pbpdL7G0wOOp1ouVKanFScW10kt19T5To8UqQqNPV6qazPe+rX7Ev8A4ScxN1HhZNNODnDXZp3fzzM011LbsSzW0q7ZmvhKwAOzOAAAAAAAAAAAAAAAAAAAAAAAABstYquqcXOWytd+CbSb9rkPfiDzHi67yUpQhR7X+mqTk51FlazSlZaavTo2tys2wtWuXZ8z/iLgsIpqFVV6yi8tOm80VJXspSWi131voQfzjz1i+INKrJQpp3jTp3UU/F9ZPzMSpwqq3Zxlf7liXDJLdNepHfut27NRl9yqhh80JytZxtr43vp87Gx/4De+hblgGr+Flr469CJTDTtW3WpUp26J9fTysbJYRuVradfYqq4KL7Rt5ZRimopfHrZpeGmpGTEtTN66+9uj9iulSu33ktL/AMLzM1YNOKa0fXz/AJ2LNOhrZuy2ehOTGF2hiXF5k3ZZdU2m2uvnubWjRhOVNpJLOlVjLXNd6u++a97W8jW06KtZbvy26bf5ubvhV7tSjaLV5L/xS1cenn7nDUjHWGjSnPSWPjFFRjBatSvOUkm3dO/e3y7fMyuF5Y1JQqN03e1P+3q7Jvu66NPxZbr0rZ1FOLacYXVllulrbTVdOh5OlJ2zb7Svra21rf5oV25jC82xKvEweaeaMWpOUu9FKpeWkk2trG35SxMMNi6FSWaSvGVleLcYtq19L/xqW8HhHUV3ldrRbknq5bybL6wFSbptKScH3Fa+abVtt7Px8yceEZ8voyE00mndNXTXVFRGfL3FcZThGnTV1FubVRN3staV/wAsW+vuSBgK86nfksitZR7rTe+dSW6NNL7mS+ntZgALuYAAAAAAAAAAAAAAAAAAAAA8lFNWaTXgzA4jwajWjGE42UXeOWysbAAy4nGcmKOse8vqvY1lflOMvihf22JJLc6KfQJzKLa3JVN/kt6dTCqckwV/iJalhkY88CvAYhO6URS5Hhsr73fiyxV5Gg+siXHgEndIsy4bvbruMQbkSz5Fj0k/proW1yJFWeZ9F038yWnww8XCvIbYTuRTHkXWTUrNq2y0/TfYy8LyS4tWqSVuqSf3JO/5Yi7T4cl0KzSExeYRquTk0tW2l12v5eBkYDk2K6OL2fVS+fQkeOAXgX6eDRHp1T6suLwfKVO1pQTs7xV5X9bm2wfL8abTjG7170m29ba3fojpo0EXY0yYrCs3lYwWCjTWiV38T/8AnoZMYpaLQ9BZTIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHlgAPHE8yAAedmh2aAA97NDIAB7lPUgAPQAAAAAAAAAAAAAAAAAB//9k='
    return results

def get_plant_with_id(id):
	results = PlantCsv.objects.get(id=id)
	if ('none' in results.image.lower()) or ("n/a" in results.image.lower()):
		results.image ='data:image/jpeg;base64,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'
	return results

def search_park_with_string(p):
    qset = Stateparks.objects.all()
    leftover = set()
    for parks in qset:
        if(p.lower() in parks.name.lower()):
            parks.image = re.sub('https','https:',str(parks.image))
            leftover.add(parks)
    return leftover

def get_park_with_dbid(dbid):
	results = Stateparks.objects.get(dbid=str(dbid))
	results.image = re.sub('https','https:',str(results.image))
	return results


def get_all_parks():
	results = Stateparks.objects.all()
	for park in results:
		park.image = re.sub('https','https:',str(park.image))
	return results

''' regular functions '''

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
def main_page(request):
    if request.method == 'GET':
        textfield =request.GET.get('search')
        if not textfield:
            template = loader.get_template('plantsite/html/mainPage.html')
            return HttpResponse(template.render({},request))
        results = search_plants_with_string(textfield)
        if not results:
            template = loader.get_template('plantsite/html/plant_list.html')
            return HttpResponse(template.render({},request))
        else:
            template = loader.get_template('plantsite/html/plant_list.html')
            context_dict = {"plant_names":results}
            return HttpResponse(template.render(context_dict,request))
    else:
        template = loader.get_template('plantsite/html/mainPage.html')
        number = request.GET.get('id')
        number = str(number)
        if number.isdigit():
            num = int(number)
            if -1 < num < 30:
                response = redirect('/plant_profile/?id=' + number)
                return response
        return HttpResponse(template.render({}, request))


class Plant(object):

    def __init__(self, name, img, url):
        self.name = name
        self.img = img
        self.url = url


def plants_each(request):
    template = loader.get_template('plantsite/html/plants_each.html')
    """
    park1 = Park("Pedernales State Park", "sp_pedernales.jpg", "/park1/")
    park2 = Park("Dinosaur Valley State Park", "sp_dinosaur_valley.jpg", "/park2/")
    park3 = Park("Daingerfield State Park", "sp_daingerfield.jpg", "/park3/")
    park4 = Park("Acton State Park", "sp_acton.jpg", "/park4/")
    parklist = [park1, park2, park3, park4]

    context_dict = {"park_list":parklist}
    """
    number = request.GET.get('id')
    prof = PlantCsv.objects.get(id=number)
    context_dict = {'profile': prof}
    #return HttpResponse(template.render(context_dict, request))
    return HttpResponse(template.render(context_dict, request))

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

    if not request.method == 'GET':
        names = get_all_plants()
        names = fix_plant_defualt(names)
        page = request.GET.get('page')
        if not page:
            context_dict = paginator_processing(names, 1)
        else:
            context_dict = paginator_processing(names, page)
        return HttpResponse(template.render(context_dict,request))

    textfield = request.GET.get('search')
    if textfield:
        results = search_plants_with_string(textfield)
        if not results:
            return HttpResponse(template.render({},request))
        else:
            results = fix_plant_defualt(results)
            context_dict = {'plant_names': results}
            return HttpResponse(template.render(context_dict,request))

    planttype_field =request.GET.get('planttype')
    water_demand_field =request.GET.get('waterdemand')
    plant_form_field =request.GET.get('plantform')
    season_field = request.GET.get('season')
    native_field = request.GET.get('native')
    lightreq_field = request.GET.get('lightreq')
    names = filter_plants_with_parameters(planttype_field, water_demand_field, plant_form_field, season_field, native_field, lightreq_field)
    names = fix_plant_defualt(names)
    page = request.GET.get('page')
    if not page:
        context_dict = paginator_processing(names, 1)
    else:
        context_dict = paginator_processing(names, page)
    return HttpResponse(template.render(context_dict,request))

def paginator_processing(names, page):
    pages = Paginator(names, 15)
    page_range = []
    mid_pages = 3
    page_goto = 1
    current = int(page)
    page_all = pages.num_pages
    try:
        names = pages.page(page)
    except PageNotAnInteger:
        names = pages.page(1)
    except EmptyPage:
        names = pages.page(paginator.num_pages)
    if page_all <= 2 + mid_pages:
        page_range = pages.page_range
    else:
        page_range += [1, page_all]
        page_range += [current-1, current, current+1]
        if current == 1 or current == page_all:
            page_range += [current+2, current-2]
        page_range = filter(lambda x: x>=1 and x<=page_all, page_range)
        page_range = sorted(list(set(page_range)))
        t = 1
        for i in range(len(page_range)-1):
            step = page_range[t]-page_range[t-1]
            if step>=2:
                if step==2:
                    page_range.insert(t,page_range[t]-1)
                else:
                    page_goto = page_range[t-1] + 1
                    page_range.insert(t,'...')
                t+=1
            t+=1
    pages.page_range_ex = page_range
    pages.page_goto = page_goto
    context_dict = {'names': names, 'pages': pages}
    return context_dict


def plant_profile_view(request):
    template = loader.get_template('plantsite/html/plants_each.html')
    number = request.GET.get('id')
    prof = get_plant_with_id(number)

    context_dict = {'profile': prof}
    return HttpResponse(template.render(context_dict,request))

#============================================
def eco_profile_view(request):
    template = loader.get_template('plantsite/html/eco_profile.html')
    dbid = request.GET.get('id')
    prof = PlantCsvEcoregions.objects.get(dbid=str(dbid))
    prof.image = prof.image.strip() #remove leading whitespace ERICK
   # keys = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    #values = ['PINEYWOODS', 'GULF PRAIRIES AND MARSHES', 'POST OAK SAVANNAH', 'BLACKLAND PRAIRIES', 'CROSS TIMBERS AND PRAIRIES', 'SOUTH TEXAS PLAINS', 'EDWARDS PLATEAU', 'ROLLING PLAINS', 'HIGH PLAINS', 'TRANS-PECOS']
    #dictionary = dict(zip(keys, values))
    plants_in_eco = prof.plants
    #plants_in_eco = re.sub(" ",'',str(plants_in_eco))
    plants_in_eco = re.sub("\[",'',str(plants_in_eco)) #gets rid of brackets
    plants_in_eco = re.sub("\]",'',str(plants_in_eco))
    plant_list = plants_in_eco.split(',') #uses comma as delimiter to split string and make a list
    plant_ids = set() #set will be used to store database objects (a query set)
    for p in plant_list:
        if not p == '':
            plant_ids.add(p)
    plants = PlantCsv.objects.filter(id__in=plant_ids)
    plants = fix_plant_defualt(plants)
    # eco_name = str(prof.ecoregion)
    # eco_name = eco_name[22:]
    #eco_name = dictionary[str(dbid)]
    #pla = PlantCsv.objects.filter(econregion=eco_name)
    context_dict = {'profile': prof, 'plants': plants}
    return HttpResponse(template.render(context_dict, request))

def park_list_view(request):
	if request.method == 'GET':
		textfield = request.GET.get('search')
		if not textfield:
			template = loader.get_template('plantsite/html/park_list.html')
			park_list = get_all_parks()
			page = request.GET.get('page')
			if not page:
				context_dict = paginator_processing(park_list, 1)
			else:
				context_dict = paginator_processing(park_list, page)
			return HttpResponse(template.render(context_dict, request))
		else:
			results = search_park_with_string(textfield)
			if not results:
				template = loader.get_template('plantsite/html/park_list.html')
				return HttpResponse(template.render({},request))
			else:
				template = loader.get_template('plantsite/html/park_list.html')
				context_dict = {'parks':results}
				return HttpResponse(template.render(context_dict,request))
	else:
		template = loader.get_template('plantsite/html/park_list.html')
		park_list = get_all_parks()
		page = request.GET.get('page')
		if not page:
			context_dict = paginator_processing(park_list, 1)
		else:
			context_dict = paginator_processing(park_list, page)
		return HttpResponse(template.render(context_dict, request))

def park_profile_view(request):
    template = loader.get_template('plantsite/html/park_profile.html')
    dbid = request.GET.get('id')
    prof = get_park_with_dbid(str(dbid))
    plants_in_park = prof.plantlist
    plants_in_park = re.sub("\[",'',str(plants_in_park)) #gets rid of brackets
    plants_in_park = re.sub("\]",'',str(plants_in_park))
    plant_list = plants_in_park.split(',') #uses comma as delimiter to split string and make a list
    plants = set() #set will be used to store database objects (a query set)
    for p in plant_list:
    	if not p == '':
    		plants.add(get_plant_with_id(str(p)))
    context_dict = {'profile': prof, 'plants':plants}
    return HttpResponse(template.render(context_dict, request))

#<img src="{{ MEDIA_URL }}{{ image.image.url }}" />
