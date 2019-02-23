from bs4 import BeautifulSoup
import lxml
import requests
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
print(listdata)