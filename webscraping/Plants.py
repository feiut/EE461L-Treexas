import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class Plants:

    def __init__(self,Sciname):
        self.SciName = Sciname
        self.Lat = 0
        self.Long = 0
        self.Econregion = ""
        self.Statepark = ""

    def geteco(self):
        web = webdriver.Chrome(executable_path=r"C:\Users\eric\Documents\chromedriver.exe")
        web.get("https://www.gbif.org/occurrence/search?has_coordinate=true&has_geospatial_issue=false&taxon_key=6&geometry=POLYGON((-112%2022,-85%2022,-85%2035,-112%2035,-112%2022))")
        search = web.find_element_by_xpath("//*[@id=\"siteSearch\"]")
        search.send_keys(Keys.CONTROL + "a")
        search.send_keys(self.SciName)
        location = web.find_element_by_xpath("//*[@id=\"main\"]/div/div/div[1]/div/div/div/section[3]/div/div[1]/div/table/tbody/tr[1]/td[4]/a")
        location.click();
        latitude=web.find_element_by_xpath("//*[@id=\"main\"]/div/div/div[1]/div/article/ng-include/section[4]/div/div[2]/div/section[6]/div[2]/table/tbody/tr[6]/td[2]")
        longitude=web.find_element_by_xpath("//*[@id=\"main\"]/div/div/div[1]/div/article/ng-include/section[4]/div/div[2]/div/section[6]/div[2]/table/tbody/tr[7]/td[2]")
        web.get("http://hicksenvplantdatabase.com/select_geocode.asp")
        lat = web.find_element_by_xpath("//*[@id=\"GetLatLong\"]/p[1]/input[1]")
        lat.send_keys(Keys.CONTROL + "a");
        lat.send_keys(latitude)
        long = web.find_element_by_xpath("//*[@id=\"GetLatLong\"]/p[1]/input[2]")
        long.send_keys(Keys.CONTROL + "a");
        long.send_keys(longitude)
        submit = web.find_element_by_xpath("//*[@id=\"GetLatLong\"]/p[2]/input")
        submit.click();
        if web.current_url != "http://hicksenvplantdatabase.com/select_geocode.asp":
            self.Lat=latitude
            self.Long=longitude
            text = web.find_element_by_xpath("//*[@id=\"maincontent\"]/form/div[2]/textarea").get_attribute("value")
            ls = text.split("-->")
            self.Econregion=ls[1]
        else:
            print(self.SciName+"Failed")
        web.close()