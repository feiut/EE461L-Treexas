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
        self.ecoregionlist=[]
    @staticmethod
    def createcsv(parklist):
        dictionary = {
            "Name": [],
            "Latitude": [],
            "Longitude": [],
            "Region": [],
            "Image": [],
            "Url": [],
            "Description": [],
            "PlantList":[],
            "Address":[],
            "Ecoregionlist":[]
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
            dictionary['Ecoregionlist'].append(entry.ecoregionlist)
        df = pd.DataFrame(dictionary)
        df.to_csv('./plant_csv_stateparks.csv')
    @staticmethod
    def createPlants(parklist,plantlist):
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
