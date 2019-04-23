import pandas as pd
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import pickle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webscraping.plant import Plant
plantlist=[]
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
web = webdriver.Chrome(executable_path=r"C:\Users\eric\Documents\chromedriver.exe",chrome_options=options)
wait = WebDriverWait(web, 5)
with open('plantlist.txt','rb') as fp:
    plantlist=pickle.load(fp)
web.get("http://www.missouribotanicalgarden.org/plantfinder/plantfindersearch.aspx")
i=0
j=0
for plant in plantlist:
    input = web.find_element_by_xpath("//*[@id=\"MainContentPlaceHolder_BasicSearchCtrl_CommonNameSearch\"]")
    input.send_keys(Keys.CONTROL+"a")
    input.send_keys(plant.sciname)
    input.send_keys(Keys.ENTER)
    try:
        web.find_element_by_xpath("//*[@id=\"MainContentPlaceHolder_SearchResultsList_SearchResultControlLeft_0_TaxonHTMLName_0\"]").click()
        if len(web.find_elements_by_xpath("//*[@id=\"MainContentPlaceHolder_CommonNameRow\"]"))!=0:
            if plant.nickname == "N/A":
                name = web.find_element_by_xpath("//*[@id=\"MainContentPlaceHolder_CommonNameRow\"]").text
                plant.nickname= name.split(':')[1]
        if len(web.find_elements_by_xpath("//*[@id=\"MainContentPlaceHolder_ZoneRow\"]")) != 0:
            if len(plant.zones)<2:
                name = web.find_element_by_xpath("//*[@id=\"MainContentPlaceHolder_ZoneRow\"]").text
                plant.zones.append(name.lower().split(':')[1].split('to')[0])
                plant.zones.append(name.lower().split(':')[1].split('to')[1])
        if len(web.find_elements_by_xpath("//*[@id=\"MainContentPlaceHolder_TypeRow\"]")) != 0:
            if plant.planttype == "N/A":
                name = web.find_element_by_xpath("//*[@id=\"MainContentPlaceHolder_TypeRow\"]").text
                plant.planttype = name.split(':')[1]
        if len(web.find_elements_by_xpath("//*[@id=\"MainContentPlaceHolder_HeightRow\"]")) != 0:
            if plant.plantheight == "N/A":
                name = web.find_element_by_xpath("//*[@id=\"MainContentPlaceHolder_HeightRow\"]").text
                plant.plantheight = name.split(':')[1]
        if len(web.find_elements_by_xpath("//*[@id=\"MainContentPlaceHolder_SpreadRow\"]")) != 0:
            if plant.plantspread == "N/A":
                name = web.find_element_by_xpath("//*[@id=\"MainContentPlaceHolder_SpreadRow\"]").text
                plant.plantspread = name.split(':')[1]
        if len(web.find_elements_by_xpath("//*[@id=\"MainContentPlaceHolder_BloomTimeRow\"]")) != 0:
            if plant.season == "N/A":
                name = web.find_element_by_xpath("//*[@id=\"MainContentPlaceHolder_BloomTimeRow\"]").text
                plant.season= name.split(':')[1]
        if len(web.find_elements_by_xpath("//*[@id=\"MainContentPlaceHolder_ColorTextRow\"]")) != 0:
            if plant.ornamentalvalue == "N/A":
                name = web.find_element_by_xpath("//*[@id=\"MainContentPlaceHolder_ColorTextRow\"]").text
                plant.ornamentalvalue = name.split(':')[1]
        if len(web.find_elements_by_xpath("//*[@id=\"MainContentPlaceHolder_SunRow\"]")) != 0:
            if plant.lightreq == "N/A":
                name = web.find_element_by_xpath("//*[@id=\"MainContentPlaceHolder_SunRow\"]").text
                plant.lightreq = name.split(':')[1]
        if len(web.find_elements_by_xpath("//*[@id=\"MainContentPlaceHolder_WaterRow\"]")) != 0:
            if plant.waterdemand == "N/A":
                name = web.find_element_by_xpath("//*[@id=\"MainContentPlaceHolder_WaterRow\"]").text
                plant.waterdemand = name.split(':')[1]
        if len(web.find_elements_by_xpath("//*[@id=\"MainContentPlaceHolder_SpreadRow\"]")) != 0:
            if plant.plantspread == "N/A":
                name = web.find_element_by_xpath("//*[@id=\"MainContentPlaceHolder_SpreadRow\"]").text
                plant.plantspread = name.split(':')[1]
        web.back()
    except:
        i+1
        print(i)
    j=j+1
    if j == 10:
        with open('plantlist.txt', 'wb') as fp:
            pickle.dump(plantlist, fp)
        j = 0
    web.back()
with open('plantlist.txt', 'wb') as fp:
    pickle.dump(plantlist, fp)