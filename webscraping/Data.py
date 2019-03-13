from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
    productdiv = data.find_element_by_class_name("product")
    if len(productdiv.find_elements_by_css_selector("span"))>0:
        if productdiv.find_element_by_css_selector("span").text=="NATIVE!":
            templist.append("Native:Yes")
        else:
            templist.append("Native:No")
    else:
        templist.append("Native:No")
    name = data.find_element_by_class_name("product-details")
    picture = data.find_element_by_class_name(("product-thumb"))
    urlinner=name.find_element_by_css_selector("a").get_attribute("href")
    url_responseinner=requests.get(urlinner)
    time.sleep(.2)
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




"""url_response = requests.get(web.current_url)
soup = BeautifulSoup(url_response,"html.parser")
listdata=[]
for data in soup("div",{"class": {"product-container col-sm-4 col-md-3 col-lg-3 mb-5"}}):
    templist = []
    if data.div.span != None:
        if data.div.span.get_text()==" Native!":
            templist.append("Native:Yes")
        else:
            templist.append("Native:No")
    else:
        templist.append("Native:No")
    name = data("div",{"class":{"product-details text-center"}})
    picture = data("div",{"class":{"product-thumb"}})
    urlinner="http://www.txsmartscape.com/plant-search/"+name[0].a['href']
    url_responseinner=requests.get(urlinner)
    soupinner = BeautifulSoup(url_responseinner.content,"html.parser")
    save=soupinner.findAll("ul",{"class": {"list theme-colored"}})
    if picture[0].a.img['src']=="plant-photos/nophoto.jpg":
        templist.append("Image: None")
    else:
        templist.append("Image:"+"http://www.txsmartscape.com/plant-search/"+picture[0].a.img['src'])
    templist.append("Name:"+name[0].a.h5.get_text())
    for i in save[0].contents:
        if i != "\n":
            #name = i.strong.string
            templist.append(i.get_text())
    listdata.append(templist)"""

dictionary = {
              "Native":[],
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

df = pd.DataFrame(dictionary)
df.to_csv('./plant_csv.csv')
print(len(listdata))
print(listdata)

