from bs4 import BeautifulSoup;
import requests;
import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
url ="https://tpwd.texas.gov/spdest/parkinfo/maps/park_maps/"
url_response = requests.get(url)
soup=BeautifulSoup(url_response.content,"html.parser")
listdata=[]
data = soup.findAll("div",{"id": {"maincontent"}});
for info in data[0].findAll("ul"):
    listofwebsite=info.findAll("li")
    for website in listofwebsite:
        templist=[]
        templist.append(website.a.get_text())
        urlinner = "https://tpwd.texas.gov"+website.a['href']
        urlinnerresponse=requests.get(urlinner)
        soupinner = BeautifulSoup(urlinnerresponse.content,"html.parser")
        data1 = soupinner.find("div",{"class": {"latlong"}})
        for direction in data1.findAll("p"):
            templist.append(direction.get_text())
        listdata.append(templist)
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
        front= "Region:"+ls[1]
        data.append(front)
        web.back();
        time.sleep(.2)
    else:
        front = "Region:N/A"
        data.append(front)
        time.sleep(.2)

dictionary ={
    "Name":[],
    "Latitude":[],
    "Longitude":[],
    "Region":[]
}
for lis in listdata:
    lis[0]="Name:"+lis[0]
    for entry in lis:
        ls = entry.split(':')
        key = ls[0]
        value = ls[1]
        dictionary[key].append(value)
df = pd.DataFrame(dictionary)
df.to_csv('./plant_csv_stateparks.csv')
print(listdata);