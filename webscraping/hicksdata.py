import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
web = webdriver.Chrome(executable_path=r"C:\Users\eric\Documents\chromedriver.exe")
web.get("http://hicksenvplantdatabase.com/species_code.asp")
listdata=[]
for i in range(1,337):
    templist=[]
    button = web.find_element_by_xpath("//*[@id=\"maincontent\"]/div[2]/div[2]/div/form/select")
    button.send_keys(str(i))
    word=""
    i=0
    valid = False
    for plantinfo in web.find_elements_by_xpath("//*[@id=\"maincontent\"]/span"):
        a=plantinfo.text
        if valid or a=="Scientific Name:" or a=="Common Name:" or a=="Ecological Distribution:"or a== "Light Tolerance:"or a=="Physical Form:"or a=="Habit:"or a=="Life Cycle:"or a=="Soil pH:"or a=="Food for Wildlife/Livestock:" or a=="Reproduction:"or a=="Notes:":
            if i == 0:
                word += plantinfo.text
                i = 1
                valid = True
            else:
                word += plantinfo.text
                templist.append(word)
                word = ""
                i = 0
                valid = False
    web.back()
    listdata.append(templist)

dictionary ={
    "Scientific Name":[],
    "Common Name":[],
    "Ecological Distribution":[],
    "Light Tolerance":[],
    "Physical Form":[],
    "Habit":[],
    "Life Cycle":[],
    "Soil pH":[],
    "Reproduction":[],
    "Notes":[]
}
for lis in listdata:
    lis[0]="Name:"+lis[0]
    for entry in lis:
        ls = entry.split(':')
        key = ls[0]
        value = ls[1]
        dictionary[key].append(value)
df = pd.DataFrame(dictionary)
df.to_csv('./plantadd_csv.csv')
print(listdata);





