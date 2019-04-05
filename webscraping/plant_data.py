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
wait = WebDriverWait(web, 60)
with open('plantlist.txt','rb') as fp:
    plantlist=pickle.load(fp)
web.get("https://www.google.com/search?q=google+docs&rlz=1C1NDCM_enUS703US703&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiRlPWU77ThAhUQD60KHRF_CBAQ_AUIECgD&biw=982&bih=792")
for i in range(len(plantlist)):
    if plantlist[i].image=="N/A" or plantlist[i].image==' None' or plantlist[i].image==None:
        wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"sbtc\"]/div/div[1]/input")))
        input = web.find_element_by_xpath("//*[@id=\"sbtc\"]/div/div[1]/input")
        input.send_keys(Keys.CONTROL + "a")
        input.send_keys(plantlist[i].sciname)
        input.send_keys(u'\ue007')
        #search = web.find_element_by_xpath("//*[@id=\"sbtc\"]/button/div/span/svg")
        #search.click()
        #wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"rg_s\"]/div[1]")))
        #picture = web.find_element_by_xpath("//*[@id=\"rg_s\"]/div[1]")
        #picture.find_element_by_css_selector("a").click()
        wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"rg_s\"]/div[1]/a[1]")))
        picture = web.find_element_by_xpath("//*[@id=\"rg_s\"]/div[1]/a[1]").get_attribute("href")
        web.get(picture)
        k=1
        while(k):
            try:
                wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"irc_cc\"]/div[2]/div[1]/div[2]/div[1]/a/img")))
                image = web.find_element_by_xpath("//*[@id=\"irc_cc\"]/div[2]/div[1]/div[2]/div[1]/a/img").get_attribute('src')
                plantlist[i].image = image
                with open('plantlist.txt', 'wb') as fp:
                    pickle.dump(plantlist,fp)
                web.back()
                k=0
            except:
                print("failed")
Plant.plantcsv(plantlist)
