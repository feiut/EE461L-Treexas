from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def txsmartscape():
    url = "http://www.txsmartscape.com/plant-search/get-plant-data.php"
    #http://www.txsmartscape.com/plant-search/plant-details.php?id=968
    #http://www.txsmartscape.com/plant-search/get-plant-data.php
    web = webdriver.Chrome(executable_path=r"C:\Users\eric\Documents\chromedriver.exe")
    web.get(url)
    button= web.find_element_by_xpath("//*[@id=\"loadmorebtn\"]/a")
    clicks = 15
    while clicks>0:
        button.click()
        time.sleep(1)
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
    plantdata=[]
    for i in range(len(listdata)-1):
        plant= Plants.Plants(plant)
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
        plantdata.append(plant)
    return plantdata






    """df = pd.DataFrame(dictionary)
    df.to_csv('./plant_csv.csv')
    print(len(listdata))
    print(listdata)"""

