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
from webscraping.plant import Plant
plantlist=[]
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
web = webdriver.Chrome(executable_path=r"C:\Users\eric\Documents\chromedriver.exe",chrome_options=options)
wait = WebDriverWait(web, 5)
with open('plantlist.txt','rb') as fp:
    plantlist=pickle.load(fp)
web.get("https://garden.org/plants/search/text/?q=+Abelia+x.+grandiflora+%27Confetti%27")
i=0
j=10
for plant in plantlist:
    wait.until(EC.presence_of_element_located((By.CLASS_NAME,"input-group")))
    input = web.find_element_by_class_name("input-group")
    input.find_element_by_css_selector("input").send_keys(Keys.CONTROL + "a")
    input.find_element_by_css_selector("input").send_keys(plant.sciname)
    input.find_element_by_css_selector("input").send_keys(Keys.ENTER)
    try:
        try:
            web.find_element_by_class_name("alert").find_element_by_css_selector("a").click()
        except:
            print("did you mean")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table")))
        table = web.find_element_by_css_selector("table")
        table.find_element_by_xpath("//tbody/tr[1]/td[2]/a").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table")))
        for tables in web.find_elements_by_css_selector("table"):
            try:
                if tables.find_element_by_css_selector("caption").text.strip().lower() == "common names:":
                    if plant.nickname == "N/A":
                        plant.nickname=tables.find_element_by_xpath("//tbody/tr[1]/td[2]").text
                if tables.find_element_by_css_selector("caption").text.strip().lower() == "general plant information (edit)":
                    table = tables
            except:
                print("caught")
        for ele in table.find_elements_by_css_selector("tr"):
            temp = ele.find_elements_by_css_selector("td")
            title = temp[0].text.strip().lower()
            if plant.planttype == "N/A":
                if title == "plant habit:":
                    plant.planttype=temp[1].text
            if plant.lifecycle == "N/A":
                if title == "life cycle:":
                    plant.lifecycle = temp[1].text
            if plant.lightreq == "N/A":
                if title == "sun requirements:":
                    plant.lightreq = temp[1].text
            if plant.waterdemand == "N/A":
                if title == "water preferences:":
                    plant.waterdemand = temp[1].text
            if plant.soil == "N/A":
                if title == "soil ph preferences:":
                    plant.soil = temp[1].text
            if plant.plantheight == "N/A":
                if title == "plant height:":
                    plant.plantheight = temp[1].text
            if plant.plantspread == "N/A":
                if title == "plant spread:":
                    plant.plantspread = temp[1].text
            if plant.wildlifevalue == "N/A":
                if title == "wildlife attractant:":
                    plant.wildlifevalue=temp[1].text
            if plant.reproduction == "N/A":
                if title == "propagation: seeds:":
                    plant.reproduction = temp[1].text
            if plant.reproduction == "N/A":
                if title == "propagation: other methods:":
                    plant.reproduction = temp[1].text
            if len(plant.zones)<2:
                if title == "minimum cold hardiness:":
                    plant.zones.append(temp[1].text)
            if len(plant.zones) < 2:
                if title == "maximum recommended zone:":
                    plant.zones.append(temp[1].text)
            if plant.endangered == "N/A":
                if title == "conservation status:":
                    plant.endangered = temp[1].text
            if plant.ornamentalvalue == "N/A":
                if title == "flower color:":
                    plant.ornamentalvalue = temp[1].text
            if plant.season == "N/A":
                if title == "flower time:":
                    plant.season = temp[1].text
            if plant.landscapeuse == "N/A":
                if title == "uses:":
                    plant.landscapeuse = temp[1].text
            if title == "toxicity:":
                if plant.edibility=="N/A":
                    plant.edibility = "toxic: " + temp[1].text
                else:
                    plant.edibility += ", toxic:"+temp[1].text
            if title == "edible parts:":
                if plant.edibility == "N/A":
                    plant.edibility = "edible:" + temp[1].text
                else:
                    plant.edibility += ", edible:"+temp[1].text


    except:
        i=i+1
        print(i)
    j=j-1
    if j==0:
        with open('plantlist.txt', 'wb') as fp:
            pickle.dump(plantlist, fp)
        j=10
    web.back()
with open('plantlist.txt', 'wb') as fp:
    pickle.dump(plantlist, fp)