from bs4 import BeautifulSoup
import lxml
import requests
import pandas as pd
url = "https://tpwd.texas.gov/huntwild/wild/wildlife_diversity/wildscapes/ecoregions/"
url_response =requests.get(url)
soup = BeautifulSoup(url_response.content,'html.parser')
listdata=[]
data = soup.findAll("div",{"id": {"maincontent"}});
for info in data[0].ul.findAll("li"):
    templist=[]
    urlinner="https://tpwd.texas.gov"+info.a['href']
    url_responseinner=requests.get(urlinner)
    soupinner = BeautifulSoup(url_responseinner.content,'html.parser')
    datainner = soupinner("div",{"id": {"maincontent"}})
    templist.append(datainner[0].h2.get_text())
    summary = ""
    for paradata in datainner[0].findAll('p'):
        summary += paradata.get_text();
    templist.append(summary)
    templist1 = []
    templist1.append(datainner[0].ul.li.strong.get_text())
    for info3 in datainner[0].ul.li.findAll("li"):
        templist1.append(info3.get_text())
    templist.append(templist1)
    templist1=[]
    for info1 in datainner[0].ul.li.next_siblings:
        if info1 !="\n":
            templist1.append(info1.strong.get_text())
            for info2 in info1.ul.findAll("li"):
                    templist1.append(info2.get_text())
            templist.append(templist1)
            templist1=[]
    listdata.append(templist)
dictionary={
    "Ecoregion":[],
    "Paragraph":[],
    "Trees":[],
    "Shrubs":[],
    "Succulents":[],
    "Vines":[],
    "Vine":[],
    "Conifers":[],
    "Grasses":[],
    "Wildflowers":[]
}
listdata[0][0]="Ecoregion 1 – " + listdata[0][0]
for lis in listdata:
    lis[0]="Ecoregion:"+lis[0]
    lis[1]="Paragraph:"+lis[1]
    """lis[2]
    lis[3]
    lis[4]
    lis[5]
    lis[6]"""
for lis in listdata:
    for entry in lis:
        if isinstance(entry,list):
            key = entry[0]
            entry.remove(entry[0])
            value = entry;
        else:
            ls=entry.split(':')
            key=ls[0]
            value=ls[1]
        dictionary[key].append(value)
        size = len(dictionary['Ecoregion'])
    for dic in dictionary:
        if len(dictionary[dic])!=size:
            dictionary[dic].append("")
df = pd.DataFrame(dictionary)
df.to_csv('./plant_csv_ecoregions.csv')

print(listdata)