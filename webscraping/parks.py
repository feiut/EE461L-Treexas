from bs4 import BeautifulSoup;
import requests;
import pandas as pd
from selenium import webdriver
import time
import pickle
from selenium.webdriver.common.keys import Keys
parklist=[]
class Parks():
    def __init__(self):
        self.name="N/A"
        self.lat=""
        self.long=""
        self.url="N/A"
        self.plantlist=[]
        self.description="N/A"
        self.image="N/A"
        self.ecoregion="N/A"
    @staticmethod
    def createcsv(list):
        dictionary = {
            "Name": [],
            "Latitude": [],
            "Longitude": [],
            "Region": [],
            "Image": [],
            "Url": [],
            "Description": []
        }
        for entry in list:
            ls = entry.name.split(':')
            key = ls[0]
            value = ls[1]
            dictionary[key].append(value)
            ls = entry.lat.split(':')
            key = ls[0]
            value = ls[1]
            dictionary[key].append(value)
            ls = entry.long.split(':')
            key = ls[0]
            value = ls[1]
            dictionary[key].append(value)
            ls = entry.url.split(':')
            key = ls[0]
            value = ls[1]
            dictionary[key].append(value)
            ls = entry.description.split(':')
            key = ls[0]
            value = ls[1]
            dictionary[key].append(value)
            ls = entry.image.split(':')
            key = ls[0]
            value = ls[1]
            dictionary[key].append(value)
            ls = entry.ecoregion.split(':')
            key = ls[0]
            value = ls[1]
            dictionary[key].append(value)
        df = pd.DataFrame(dictionary)
        df.to_csv('./plant_csv_stateparks.csv')
    """def createPlants(self):
        for entry in plantlist"""

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
    web = webdriver.Chrome(executable_path=r"C:\Users\eric\Documents\chromedriver.exe")
    web.get("http://hicksenvplantdatabase.com/select_geocode.asp")
    for data in listdata:
        latitude = data[1].split(":")
        lat = web.find_element_by_xpath("//*[@id=\"GetLatLong\"]/p[1]/input[1]")
        lat.send_keys(Keys.CONTROL + "a");
        lat.send_keys(latitude[1])
        longitude = data[2].split(":")
        long = web.find_element_by_xpath("//*[@id=\"GetLatLong\"]/p[1]/input[2]")
        long.send_keys(Keys.CONTROL + "a");
        long.send_keys(longitude[1])
        submit = web.find_element_by_xpath("//*[@id=\"GetLatLong\"]/p[2]/input")
        submit.click();
        time.sleep(.2)
        if web.current_url != "http://hicksenvplantdatabase.com/select_geocode.asp":
            text = web.find_element_by_xpath("//*[@id=\"maincontent\"]/form/div[2]/textarea").get_attribute("value")
            ls = text.split("-->")
            front = "Region:" + ls[1]
            data.append(front)
            web.back();
            time.sleep(.2)
        else:
            front = "Region:N/A"
            data.append(front)
            time.sleep(.2)

    dictionary = {
        "Name": [],
        "Latitude": [],
        "Longitude": [],
        "Region": [],
        "Image":[],
        "Url":[],
        "Description":[]
    }
    for lis in listdata:
        lis[0] = "Name:" + lis[0]
        for entry in lis:
            ls = entry.split(':')
            key = ls[0]
            value = ls[1]
            dictionary[key].append(value)
    for i in range(len(listdata)) :
        p = Parks()
        p.name=dictionary['Name'][i];
        p.image=dictionary['Image'][i]
        p.description=dictionary['Description'][i]
        p.ecoregion=dictionary['Region'][i]
        p.lat=dictionary['Latitude'][i]
        p.long=dictionary['Longitude'][i]
        p.url=dictionary['Url'][i]
        parklist.append(p)
stateParks()
with open('parklist.txt','wb') as fp:
    pickle.dump(parklist,fp)
Parks.createcsv(parklist)
