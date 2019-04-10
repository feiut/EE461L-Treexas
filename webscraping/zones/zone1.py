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
web.get("https://garden.org/plants/search/text/?q=+Abelia+x.+grandiflora+%27Confetti%27")
i=0
for plant in plantlist:
    input = web.find_element_by_xpath("//*[@id=\"ngabody\]/div[2]/div[1]/form/div/input")
    input.send_keys(Keys.CONTROL + "a")
    input.send_keys(plant.sciname)
    try:
        web.find_element_by_xpath("//*[@id=\"ngabody\"]/div[2]/div[1]/table/tbody/tr/td[2]/a").click()

    except:
        i=i+1
        print(i)
with open('plantlist.txt', 'wb') as fp:
    pickle.dump(plantlist, fp)