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
        self.edibility="N/A"
        self.zones ="N/A"


    def geteco(self,web):
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
    @staticmethod
    def plantcsv(plantlist):
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
            # "note": [],
            "sciname": [],
            "lat": [],
            "long": [],
            "econregion": [],
            "statepark": [],
            "lifecycle": [],
            "edibility": [],
            "zone":[]
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
            # dictionary['note'].append(plant.note)
            dictionary['sciname'].append(plant.sciname)
            dictionary['lat'].append(plant.lat)
            dictionary['long'].append(plant.long)
            dictionary['econregion'].append(plant.econregion)
            dictionary['statepark'].append(plant.statepark)
            dictionary['lifecycle'].append(plant.lifecycle)
            dictionary['edibility'].append(plant.edibility)
            dictionary['zone'].append(plant.zones)
        df = pd.DataFrame(dictionary)
        df.to_csv('./plant_csv.csv')