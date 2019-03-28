import pandas as pd
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import pickle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
plantlist = []
parklist=[]
web = webdriver.Chrome(executable_path=r"C:\Users\eric\Documents\chromedriver.exe")
class Plant:
    def __init__(self):
        self.nativeadapted = "N/A"
        self.image="N/A"
        self.name = "N/A"
        self.nickname="N/A"
        self.planttype="N/A"
        self.lightreq="N/A"
        self.waterdemand="N/A"
        self.landscapeuse="N/A"
        self.ornamentalvalue="N/A"
        self.wildlifevalue="N/A"
        self.season="N/A"
        self.plantform="N/A"
        self.plantspread="N/A"
        self.plantheight="N/A"
        self.deciduousevergreen="N/A"
        self.soil="N/A"
        self.reproduction="N/A"
        self.note="N/A"
        self.sciname = "N/A"
        self.lat = "N/A"
        self.long = "N/A"
        self.econregion = "N/A"
        self.statepark = []
        self.lifecycle="N/A"


    def geteco(self):
        wait = WebDriverWait(web,10)
        web.get("https://www.gbif.org/occurrence/search?has_coordinate=true&has_geospatial_issue=false&taxon_key=6&geometry=POLYGON((-112%2022,-85%2022,-85%2035,-112%2035,-112%2022))")
        #time.sleep(4)
        wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id=\"siteSearch\"]')))
        search =web.find_element_by_xpath("//*[@id=\"siteSearch\"]")
        search.send_keys(Keys.CONTROL + "a")
        search.send_keys(self.sciname)
        submit = web.find_element_by_xpath("//*[@id=\"site-search\"]/div/ng-transclude/div/div[1]/form/a")
        submit.click()
        #time.sleep(4)
        b = True
        while b:
            try:
                wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"main\"]/div/div/div[1]/div/div/div/section[1]/div/div/div/nav/span[2]/span")))
                st = web.find_element_by_xpath("//*[@id=\"main\"]/div/div/div[1]/div/div/div/section[1]/div/div/div/nav/span[2]/span").text
                if (st == "0 RESULTS"):
                    return "error"
                wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id=\"main\"]/div/div/div[1]/div/div/div/section[3]/div/div[1]/div/table/tbody/tr[1]/td[4]/a")))
                b=False;
            except:
                submit = web.find_element_by_xpath("//*[@id=\"site-search\"]/div/ng-transclude/div/div[1]/form/a")
                submit.click()
        location = web.find_element_by_xpath("//*[@id=\"main\"]/div/div/div[1]/div/div/div/section[3]/div/div[1]/div/table/tbody/tr[1]/td[4]/a").text
        l=location.split(',')
        #time.sleep(4)
        #wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"main\"]/div/div/div[1]/div/article/ng-include/section[4]/div/div[2]/div/section[6]/div[2]/table/tbody/tr[6]/td[2]")))
        latitude=l[0][:-1].strip()
        longitude=l[1][:-1].strip()
        self.lat = latitude
        self.long = longitude
        if self.econregion == "N/A":
            web.get("http://hicksenvplantdatabase.com/select_geocode.asp")
            #time.sleep(.5)
            wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"GetLatLong\"]/p[1]/input[1]")))
            lat = web.find_element_by_xpath("//*[@id=\"GetLatLong\"]/p[1]/input[1]")
            lat.send_keys(Keys.CONTROL + "a")
            lat.send_keys(latitude)

            wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"GetLatLong\"]/p[1]/input[2]")))
            try:
                long = web.find_element_by_xpath("//*[@id=\"GetLatLong\"]/p[1]/input[2]")
                long.send_keys(Keys.CONTROL + "a")
                long.send_keys(longitude)
                submit = web.find_element_by_xpath("//*[@id=\"GetLatLong\"]/p[2]/input")
                submit.click()
                WebDriverWait(web, 3).until(EC.alert_is_present(),
                                            'Timed out waiting for PA creation ' + 'confirmation popup to appear.')
                alert = web.switch_to.alert
                alert.accept()
            except TimeoutException:
                print("no alert")
                print(self.sciname)
            except:
                try:
                    WebDriverWait(web, 3).until(EC.alert_is_present(),
                                                'Timed out waiting for PA creation ' + 'confirmation popup to appear.')
                    alert = web.switch_to.alert
                    alert.accept()
                    print("error")
                except TimeoutException:
                    print("shouldnt happen")
            if web.current_url != "http://hicksenvplantdatabase.com/select_geocode.asp":
                text = web.find_element_by_xpath("//*[@id=\"maincontent\"]/form/div[2]/textarea").get_attribute("value")
                ls = text.split("-->")
                self.econregion=ls[1]
class Parks():
    def __init__(self):
        self.name="N/A"
        self.lat=""
        self.long=""
        self.url="N/A"
        self.parkplantlist=[]
        self.description="N/A"
        self.image="N/A"
        self.ecoregion="N/A"
        self.address="N/A"
    @staticmethod
    def createcsv():
        dictionary = {
            "Name": [],
            "Latitude": [],
            "Longitude": [],
            "Region": [],
            "Image": [],
            "Url": [],
            "Description": [],
            "PlantList":[],
            "Address":[]
        }
        for entry in parklist:
            dictionary['Name'].append(entry.name)
            dictionary['Latitude'].append(entry.lat)
            dictionary['Longitude'].append(entry.long)
            dictionary['Region'].append(entry.ecoregion)
            dictionary['Image'].append(entry.image)
            dictionary['Url'].append(entry.url)
            dictionary['Description'].append(entry.description)
            dictionary['Address'].append(entry.address)
            dictionary['PlantList'].append(entry.parkplantlist)
        df = pd.DataFrame(dictionary)
        df.to_csv('./plant_csv_stateparks.csv')
    @staticmethod
    def createPlants():
        for i in range(len(plantlist)):
            plantlist[i].statepark=[]
        for j in range(len(parklist)):
            parklist[j].parkplantlist=[]
            for i in range(len(plantlist)):
                if(plantlist[i].long!="N/A" and plantlist[i].lat!="N/A"):
                    plantlong=abs(float(plantlist[i].long))
                    plantlat=abs(float(plantlist[i].lat))
                    parklong=abs(float(parklist[j].long))
                    parklat=abs(float(parklist[j].lat))
                    if abs(plantlong-parklong)<.5 and abs(plantlat-parklat)<.5:
                        parklist[j].parkplantlist.append(i)
                        plantlist[i].statepark.append(j)

def stateParks():
    url = "https://tpwd.texas.gov/spdest/parkinfo/maps/park_maps/"
    url_response = requests.get(url)
    soup = BeautifulSoup(url_response.content, "html.parser")
    listdata = []
    data = soup.findAll("div", {"id": {"maincontent"}});
    for info in data[0].findAll("ul"):
        listofwebsite = info.findAll("li")
        for website in listofwebsite:
            templist = []
            templist.append(website.a.get_text())
            urlinner = "https://tpwd.texas.gov" + website.a['href']
            urlinner = urlinner[:-4]
            templist.append("Url:" + urlinner)
            urlinnerresponse = requests.get(urlinner)
            soupinner = BeautifulSoup(urlinnerresponse.content, "html.parser")
            data2 = soupinner.find("address")
            templist.append("Address:" + data2.text)
            data1 = soupinner.find("div", {"class": {"latlong"}})
            for direction in data1.findAll("p"):
                templist.append(direction.get_text())
            data3 = soupinner.find("div", {"class": {"rotator-content"}})
            templist.append("Image: " + data3.img['src'])
            data4=soupinner.find("div", {"id": {"content-text"}})
            templist.append("Description: "+data4.p.text)
            listdata.append(templist)
    print(listdata)
    web.get("http://hicksenvplantdatabase.com/select_geocode.asp")
    for data in listdata:
        latitude = data[3].split(":")
        WebDriverWait(web,5).until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"GetLatLong\"]/p[1]/input[1]")))
        lat = web.find_element_by_xpath("//*[@id=\"GetLatLong\"]/p[1]/input[1]")
        lat.send_keys(Keys.CONTROL + "a");
        lat.send_keys(latitude[1])
        longitude = data[4].split(":")
        long = web.find_element_by_xpath("//*[@id=\"GetLatLong\"]/p[1]/input[2]")
        long.send_keys(Keys.CONTROL + "a");
        long.send_keys(longitude[1])
        submit = web.find_element_by_xpath("//*[@id=\"GetLatLong\"]/p[2]/input")
        submit.click();
        if web.current_url != "http://hicksenvplantdatabase.com/select_geocode.asp":
            WebDriverWait(web,5).until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"maincontent\"]/form/div[2]/textarea")))
            text = web.find_element_by_xpath("//*[@id=\"maincontent\"]/form/div[2]/textarea").get_attribute("value")
            ls = text.split("-->")
            front = "Region:" + ls[1]
            data.append(front)
            web.back();
        else:
            front = "Region:N/A"
            data.append(front)

    dictionary = {
        "Name": [],
        "Latitude": [],
        "Longitude": [],
        "Region": [],
        "Image":[],
        "Url":[],
        "Description":[],
        "Address":[]
    }
    for lis in listdata:
        lis[0] = "Name:" + lis[0]
        for entry in lis:
            ls = entry.split(':')
            if len(ls)>2:
                key=ls[0]
                value=ls[1]+ls[2]
            else:
                key = ls[0]
                value = ls[1]
            dictionary[key].append(value)
    for i in range(len(listdata)) :
        p = Parks()
        p.name=dictionary['Name'][i];
        p.image=dictionary['Image'][i]
        p.description=dictionary['Description'][i]
        if p.name[1]=="Bentsen-Rio Grande Valley State Park":
            p.ecoregion="Region:SOUTH TEXAS PLAINS"
        elif p.name=="Falcon State Park":
            p.ecoregion="Region:SOUTH TEXAS PLAINS"
        elif p.name == "Galveston Island State Park":
            p.ecoregion = "Region:GULF PRAIRIES AND MARSHES"
        elif p.name == "Goose Island State Park":
            p.ecoregion = "Region:GULF PRAIRIES AND MARSHES"
        else:
            p.ecoregion=dictionary['Region'][i]
        p.lat=dictionary['Latitude'][i]
        p.long=dictionary['Longitude'][i]
        p.url=dictionary['Url'][i]
        parklist.append(p)
def txsmartscape():
    url = "http://www.txsmartscape.com/plant-search/get-plant-data.php"
    #http://www.txsmartscape.com/plant-search/plant-details.php?id=968
    #http://www.txsmartscape.com/plant-search/get-plant-data.php
    web.get(url)
    button= web.find_element_by_xpath("//*[@id=\"loadmorebtn\"]/a")
    clicks = 15
    while clicks>0:
        button.click()
        time.sleep(.8)
        clicks= clicks -1
    listdata=[]
    for data in web.find_elements_by_xpath("//*[@id=\"moreresults\"]/div"):
        templist = []
        name = data.find_element_by_class_name("product-details")
        picture = data.find_element_by_class_name(("product-thumb"))
        urlinner=name.find_element_by_css_selector("a").get_attribute("href")
        url_responseinner=requests.get(urlinner)
        #time.sleep(.2)
        soupinner = BeautifulSoup(url_responseinner.content,"html.parser")
        save=soupinner.findAll("ul",{"class": {"list theme-colored"}})
        if picture.find_element_by_css_selector("a").find_element_by_css_selector("img").get_attribute("src")=="http://www.txsmartscape.com/plant-search/plant-photos/nophoto.jpg":
            templist.append("Image: None")
        else:
            templist.append("Image:"+picture.find_element_by_css_selector("a").find_element_by_css_selector("img").get_attribute("src"))
        templist.append("Name:"+name.find_element_by_css_selector("a").find_element_by_css_selector("h5").text)
        for i in save[0].contents:
            if i != "\n":
                #name = i.strong.string
                templist.append(i.get_text())
        listdata.append(templist)
    dictionary = {
                  "Image":[],
                  "Name":[],
                  "Also Known As": [],
                  "Botanical Name": [],
                  "Plant Type": [],
                  "Light Requirement": [],
                  "Water Demand": [],
                  "Landscape Use": [],
                  "Ornamental Value": [],
                  "Native/Adapted": [],
                  "Wildlife Value": [],
                  "Season": [],
                  "Deciduous/Evergreen": [],
                  "Plant Form": [],
                  "Plant Spread": [],
                  "Plant Height": []
                }

    for lis in listdata:
        boo=False
        for entry in lis:
            ls = entry.split(':')
            key = ls[0]
            if len(ls)==3:
                value = ls[1]+":"+ls[2]
            else:
                value = ls[1]
            if(key == "Also Known As"):
                boo = True
            try:
                dictionary[key].append(value)
            except KeyError:
                print(key)
                print(value)
                print('Didnt work')
                print(dictionary)
                print(lis)
                print()
        if(not boo):
            dictionary["Also Known As"].append("NA")
    for i in range(len(listdata)):
        plant = Plant()
        plant.image=dictionary['Image'][i]
        plant.name = dictionary['Name'][i]
        plant.nickname = dictionary['Also Known As'][i]
        plant.sciname = dictionary['Botanical Name'][i]
        plant.planttype = dictionary['Plant Type'][i]
        plant.lightreq = dictionary['Light Requirement'][i]
        plant.waterdemand = dictionary['Water Demand'][i]
        plant.landscapeuse = dictionary['Landscape Use'][i]
        plant.ornamentalvalue=dictionary['Ornamental Value'][i]
        plant.nativeadapted = dictionary['Native/Adapted'][i]
        plant.wildlifevalue = dictionary['Wildlife Value'][i]
        plant.season=dictionary['Season'][i]
        plant.deciduousevergreen = dictionary['Deciduous/Evergreen'][i]
        plant.plantform= dictionary['Plant Form'][i]
        plant.plantheight= dictionary['Plant Height'][i]
        plant.plantspread= dictionary['Plant Spread'][i]
        plantlist.append(plant)

def hicksdata():
    web.get("http://hicksenvplantdatabase.com/species_code.asp")
    listdata = []
    for i in range(1, 337):
        templist = []
        WebDriverWait(web,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"maincontent\"]/div[2]/div[2]/div/form/select")))
        button = web.find_element_by_xpath("//*[@id=\"maincontent\"]/div[2]/div[2]/div/form/select")
        button.send_keys(str(i))
        word = ""
        i = 0
        valid = False
        WebDriverWait(web,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"maincontent\"]/span")))
        for plantinfo in web.find_elements_by_xpath("//*[@id=\"maincontent\"]/span"):
            a = plantinfo.text
            if valid or a=="Vegetative Growth Period:" or a == "Scientific Name:" or a == "Common Name:" or a == "Ecological Distribution:" or a == "Light Tolerance:" or a == "Physical Form:" or a == "Habit:" or a == "Life Cycle:" or a == "Soil pH:" or a == "Food for Wildlife/Livestock:" or a == "Reproduction:" or a == "Notes:":
                if i == 0:
                    word += plantinfo.text
                    i = 1
                    valid = True
                else:
                    word += plantinfo.text
                    templist.append(word)
                    word = ""
                    i = 0
                    valid = False
        web.back()
        listdata.append(templist)
    dictionary = {
        "Scientific Name": [],
        "Common Name": [],
        "Ecological Distribution": [],
        "Light Tolerance": [],
        "Physical Form": [],
        "Habit": [],
        "Life Cycle": [],
        "Soil pH": [],
        "Reproduction": [],
        "Food for Wildlife/Livestock":[],
        "Vegetative Growth Period":[],
        "Notes": []
    }
    for lis in listdata:
        for entry in lis:
            ls = entry.split(':')
            key = ls[0]
            value = ls[1]
            dictionary[key].append(value)
    for i in range(len(listdata)):
        plant=Plant()
        plant.sciname=dictionary['Scientific Name'][i]
        plant.name=dictionary['Common Name'][i]
        plant.econregion = dictionary['Ecological Distribution'][i]
        plant.lightreq=dictionary['Light Tolerance'][i]
        plant.planttype=dictionary['Physical Form'][i]
        plant.deciduousevergreen=dictionary['Habit'][i]
        plant.lifecycle=dictionary['Life Cycle'][i]
        plant.soil=dictionary['Soil pH'][i]
        plant.reproduction=dictionary['Reproduction'][i]
        plant.wildlifevalue=dictionary['Food for Wildlife/Livestock'][i]
        plant.note=dictionary['Notes'][i]
        plant.season = dictionary['Vegetative Growth Period'][i]
        plantlist.append(plant)
def generateplantlist():
    txsmartscape()
    with open('plantlist.txt', 'wb') as fp:
        pickle.dump(plantlist, fp)
    hicksdata()
    with open('plantlist.txt', 'wb') as fp:
        pickle.dump(plantlist, fp)
def plantcsv():
    dictionary = {
        "nativeadapted": [],
        "image": [],
        "name": [],
        "nickname": [],
        "planttype": [],
        "lightreq": [],
        "waterdemand": [],
        "landscapeuse": [],
        "ornamentalvalue": [],
        "wildlifevalue": [],
        "season": [],
        "plantform": [],
        "plantspread": [],
        "plantheight": [],
        "deciduousevergreen": [],
        "soil": [],
        "reproduction": [],
        "note": [],
        "sciname": [],
        "lat": [],
        "long": [],
        "econregion": [],
        "statepark": [],
        "lifecycle": []
    }
    for plant in plantlist:
        dictionary['nativeadapted'].append(plant.nativeadapted)
        dictionary['image'].append(plant.image)
        dictionary['name'].append(plant.name)
        dictionary['nickname'].append(plant.nickname)
        dictionary['planttype'].append(plant.planttype)
        dictionary['lightreq'].append(plant.lightreq)
        dictionary['waterdemand'].append(plant.waterdemand)
        dictionary['reproduction'].append(plant.reproduction)
        dictionary['landscapeuse'].append(plant.landscapeuse)
        dictionary['ornamentalvalue'].append(plant.ornamentalvalue)
        dictionary['wildlifevalue'].append(plant.wildlifevalue)
        dictionary['season'].append(plant.season)
        dictionary['plantform'].append(plant.plantform)
        dictionary['plantspread'].append(plant.plantspread)
        dictionary['plantheight'].append(plant.plantheight)
        dictionary['deciduousevergreen'].append(plant.deciduousevergreen)
        dictionary['soil'].append(plant.soil)
        dictionary['note'].append(plant.note)
        dictionary['sciname'].append(plant.sciname)
        dictionary['lat'].append(plant.lat)
        dictionary['long'].append(plant.long)
        dictionary['econregion'].append(plant.econregion)
        dictionary['statepark'].append(plant.statepark)
        dictionary['lifecycle'].append(plant.lifecycle)
    df = pd.DataFrame(dictionary)
    df.to_csv('./plant_csv.csv')




#maincode

#with open('plantlist.txt', 'rb') as fp:
#    plantlist=pickle.load(fp)
#stateParks()
#with open('parklist.txt', 'wb') as fp:
#    pickle.dump(parklist, fp)
with open('parklist.txt','rb') as fp:
    parklist=pickle.load(fp)
with open('plantlist.txt','rb') as fp:
    plantlist=pickle.load(fp)
Parks.createPlants()
with open('parklist.txt', 'wb') as fp:
    pickle.dump(parklist, fp)
with open('plantlist.txt', 'wb') as fp:
   pickle.dump(plantlist,fp)
Parks.createcsv()
plantcsv();
#generateplantlist()
#for data in plantlist:
"""for data in plantlist:
    data.geteco()
with open('plantlist.txt','wb') as fp:
    pickle.dump(plantlist,fp)"""
web.close()