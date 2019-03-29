from bs4 import BeautifulSoup
import lxml
import requests
import pandas as pd
from selenium import webdriver
import time
import pickle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
web = webdriver.Chrome(executable_path=r"C:\Users\eric\Documents\chromedriver.exe")
class Ecoregions:
    def __init__(self):
        self.name=""
        self.plantlist=[]
        self.stateparklist=[]
        self.description=""
        self.image=""
        self.trees=""
        self.shrubs=""
        self.succulent=""
        self.vines=""
        self.vine=""
        self.conifers=""
        self.grasses=""
        self.wildflowers=""
def createEcoRegions():
    url = "https://tpwd.texas.gov/huntwild/wild/wildlife_diversity/wildscapes/ecoregions/"
    url_response = requests.get(url)
    soup = BeautifulSoup(url_response.content, 'html.parser')
    listdata = []
    data = soup.findAll("div", {"id": {"maincontent"}})
    for info in data[0].ul.findAll("li"):
        templist = []
        urlinner = "https://tpwd.texas.gov" + info.a['href']
        url_responseinner = requests.get(urlinner)
        soupinner = BeautifulSoup(url_responseinner.content, 'html.parser')
        datainner = soupinner("div", {"id": {"maincontent"}})
        templist.append(datainner[0].h2.get_text())
        summary = ""
        for paradata in datainner[0].findAll('p'):
            summary += paradata.get_text();
        templist.append(summary)
        templist1 = []
        templist1.append(datainner[0].ul.li.strong.get_text())
        for info3 in datainner[0].ul.li.findAll("li"):
            templist1.append(info3.get_text())
        templist.append(templist1)
        templist1 = []
        for info1 in datainner[0].ul.li.next_siblings:
            if info1 != "\n":
                templist1.append(info1.strong.get_text())
                for info2 in info1.ul.findAll("li"):
                    templist1.append(info2.get_text())
                templist.append(templist1)
                templist1 = []
        listdata.append(templist)
    dictionary = {
        "Ecoregion": [],
        "Paragraph": [],
        "Trees": [],
        "Shrubs": [],
        "Succulents": [],
        "Vines": [],
        "Vine": [],
        "Conifers": [],
        "Grasses": [],
        "Wildflowers": [],
        "Image": []
    }
    listdata[0][0] = "Ecoregion 1 – " + listdata[0][0]
    for lis in listdata:
        lis[0] = "Ecoregion:" + lis[0]
        lis[1] = "Paragraph:" + lis[1]
        """lis[2]
        lis[3]
        lis[4]
        lis[5]
        lis[6]"""
    listdata[0].append("Image: eco_pineywoods.png")
    listdata[1].append("Image: eco_marshes.png")
    listdata[2].append("Image: eco_postoaksavanah.jpg")
    listdata[3].append("Image: eco_blacklandprairie.jpg")
    listdata[4].append("Image: eco_crosstimbers.png")
    listdata[5].append("Image: eco_southplains.png")
    listdata[6].append("Image:eco_edwards.png")
    listdata[7].append("Image:eco_rollingplains.jpg")
    listdata[8].append("Image:eco_highplains.png")
    listdata[9].append("Image:eco_transpecos.jpg")
    for lis in listdata:
        for entry in lis:
            if isinstance(entry, list):
                key = entry[0]
                entry.remove(entry[0])
                value = entry;
            else:
                ls = entry.split(':')
                key = ls[0]
                value = ls[1]
            dictionary[key].append(value)
            size = len(dictionary['Ecoregion'])
        for dic in dictionary:
            if len(dictionary[dic]) != size:
                dictionary[dic].append("")
    for i in range(len(listdata)):
        ecoregion = Ecoregions()
        ecoregion.name=dictionary['Ecoregion'][i]
        ecoregion.image=dictionary['Image'][i]
        ecoregion.description=dictionary['Paragraph'][i]
        ecoregion.conifers=dictionary['Conifers'][i]
        ecoregion.grasses=dictionary['Grasses'][i]
        ecoregion.shrubs=dictionary['Shrubs'][i]
        ecoregion.succulent=dictionary['Succulents'][i]
        ecoregion.trees=dictionary['Trees'][i]
        ecoregion.vine=dictionary['Vine'][i]
        ecoregion.vines=dictionary['Vines'][i]
        ecoregion.wildflowers=dictionary['Wildflowers'][i]
        ecoregionlist.append(ecoregion)
    """df = pd.DataFrame(dictionary)
    df.to_csv('./plant_csv_ecoregions.csv')"""
def createcsv():
    dictionary={
         "Ecoregion": [],
         "Paragraph": [],
         "Trees": [],
         "Shrubs": [],
         "Succulents": [],
         "Vines": [],
         "Vine": [],
         "Conifers": [],
         "Grasses": [],
         "Wildflowers": [],
         "Image": [],
         "StateParks":[],
         "Plants":[]
    }
    for eco in ecoregionlist:
        dictionary['Ecoregion'].append(eco.name)
        dictionary['Paragraph'].append(eco.description)
        dictionary['Trees'].append(eco.trees)
        dictionary['Shrubs'].append(eco.shrubs)
        dictionary['Succulents'].append(eco.succulent)
        dictionary['Vines'].append(eco.vines)
        dictionary['Vine'].append(eco.vine)
        dictionary['Conifers'].append(eco.conifers)
        dictionary['Grasses'].append(eco.grasses)
        dictionary['Wildflowers'].append(eco.wildflowers)
        dictionary['Image'].append(eco.image)
        dictionary['StateParks'].append(eco.stateparklist)
        dictionary['Plants'].append(eco.plantlist)
    df = pd.DataFrame(dictionary)
    df.to_csv('./plant_csv_ecoregions.csv')


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
ecoregionlist=[]
plantlist=[]
parklist=[]
createEcoRegions()
with open('ecoregionlist.txt', 'wb') as fp:
    pickle.dump(ecoregionlist, fp)
with open('ecoregionlist.txt', 'rb') as fp:
    ecoregionlist=pickle.load(fp)
with open('plantlist.txt', 'rb') as fp:
    plantlist=pickle.load(fp)
with open('parklist.txt', 'rb') as fp:
    parklist=pickle.load(fp)
for i in range(len(ecoregionlist)):
    for j in range(len(plantlist)):
        plantregion=plantlist[j].econregion
        if plantregion != "N/A":
            plantreg=plantregion.split(',')
            for entry in plantreg:
                entry=entry.strip()
                if i==0 and entry=="PINEYWOODS":
                    ecoregionlist[i].plantlist.append(j)
                if i == 1 and entry =="GULF PRAIRIES AND MARSHES":
                    ecoregionlist[i].plantlist.append(j)
                if i == 2 and entry =="POST OAK SAVANNAH":
                    ecoregionlist[i].plantlist.append(j)
                if i == 3 and entry =="BLACKLAND PRAIRIES":
                    ecoregionlist[i].plantlist.append(j)
                if i == 4 and entry =="CROSS TIMBERS AND PRAIRIES":
                    ecoregionlist[i].plantlist.append(j)
                if i == 5 and entry =="SOUTH TEXAS PLAINS":
                    ecoregionlist[i].plantlist.append(j)
                if i == 6 and entry =="EDWARDS PLATEAU":
                    ecoregionlist[i].plantlist.append(j)
                if i == 7 and entry =="ROLLING PLAINS":
                    ecoregionlist[i].plantlist.append(j)
                if i == 8 and entry =="HIGH PLAINS":
                    ecoregionlist[i].plantlist.append(j)
                if i == 9 and entry =="TRANS-PECOS":
                    ecoregionlist[i].plantlist.append(j)


for i in range(len(ecoregionlist)):
    for j in range(len(parklist)):
        entry = parklist[j].ecoregion.strip()
        if i == 0 and entry == "PINEYWOODS":
            ecoregionlist[i].stateparklist.append(j)
        if i == 1 and entry == "GULF PRAIRIES AND MARSHES":
            ecoregionlist[i].stateparklist.append(j)
        if i == 2 and entry == "POST OAK SAVANNAH":
            ecoregionlist[i].stateparklist.append(j)
        if i == 3 and entry == "BLACKLAND PRAIRIES":
            ecoregionlist[i].stateparklist.append(j)
        if i == 4 and entry == "CROSS TIMBERS AND PRAIRIES":
            ecoregionlist[i].stateparklist.append(j)
        if i == 5 and entry == "SOUTH TEXAS PLAINS":
            ecoregionlist[i].stateparklist.append(j)
        if i == 6 and entry == "EDWARDS PLATEAU":
            ecoregionlist[i].stateparklist.append(j)
        if i == 7 and entry == "ROLLING PLAINS":
            ecoregionlist[i].stateparklist.append(j)
        if i == 8 and entry == "HIGH PLAINS":
            ecoregionlist[i].stateparklist.append(j)
        if i == 9 and entry == "TRANS-PECOS":
            ecoregionlist[i].stateparklist.append(j)
with open('ecoregionlist.txt', 'wb') as fp:
    pickle.dump(ecoregionlist, fp)
createcsv()
print()