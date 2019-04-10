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
wait = WebDriverWait(web, 10)
with open('plantlist.txt','rb') as fp:
    plantlist=pickle.load(fp)
web.get("http://poisonousplants.ansci.cornell.edu/php/plants.php")
i=0
for plant in plantlist:
    if plant.edibility=="N/A":
        input=web.find_element_by_xpath("//*[@id=\"main\"]/div/form/table[1]/tbody/tr[1]/td[2]/input")
        input.send_keys(Keys.CONTROL + "a")
        input.send_keys(plant.sciname)
        web.find_element_by_xpath("//*[@id=\"main\"]/div/form/table[2]/tbody/tr[1]/td/input[1]").click()
        try:
            if len(web.find_elements_by_xpath("//*[@id=\"main\"]/div/table/tbody/tr[2]/td[2]")) != 0:
                plant.edibility="poisonous"
        except:
            i=i+1
            print(i)
        web.back()
with open('plantlist.txt','wb') as fp:
    pickle.dump(plantlist,fp)
