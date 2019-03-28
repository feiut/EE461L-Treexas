from bs4 import BeautifulSoup
import lxml
import requests
import pickle
import pandas as pd
ecoregionlist=[]
class Ecoregions:
    def __init__(self):
        self.name=""
        self.plantlist=[]
        self.description=""
        self.image=""
        self.trees=""
        self.shrubs=""
        self.succulent=""
        self.vines=""
        self.vine=""
        self.conifers=""
        self.grasses=""
        self.wildflowers=""
def createEcoRegions():
    url = "https://tpwd.texas.gov/huntwild/wild/wildlife_diversity/wildscapes/ecoregions/"
    url_response = requests.get(url)
    soup = BeautifulSoup(url_response.content, 'html.parser')
    listdata = []
    data = soup.findAll("div", {"id": {"maincontent"}});
    for info in data[0].ul.findAll("li"):
        templist = []
        urlinner = "https://tpwd.texas.gov" + info.a['href']
        url_responseinner = requests.get(urlinner)
        soupinner = BeautifulSoup(url_responseinner.content, 'html.parser')
        datainner = soupinner("div", {"id": {"maincontent"}})
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
        templist1 = []
        for info1 in datainner[0].ul.li.next_siblings:
            if info1 != "\n":
                templist1.append(info1.strong.get_text())
                for info2 in info1.ul.findAll("li"):
                    templist1.append(info2.get_text())
                templist.append(templist1)
                templist1 = []
        listdata.append(templist)
    dictionary = {
        "Ecoregion": [],
        "Paragraph": [],
        "Trees": [],
        "Shrubs": [],
        "Succulents": [],
        "Vines": [],
        "Vine": [],
        "Conifers": [],
        "Grasses": [],
        "Wildflowers": [],
        "Image": []
    }
    listdata[0][0] = "Ecoregion 1 – " + listdata[0][0]
    for lis in listdata:
        lis[0] = "Ecoregion:" + lis[0]
        lis[1] = "Paragraph:" + lis[1]
        """lis[2]
        lis[3]
        lis[4]
        lis[5]
        lis[6]"""
    listdata[0].append("Image: eco_pineywoods.png")
    listdata[1].append("Image: eco_marshes.png")
    listdata[2].append("Image: eco_postoaksavanah.jpg")
    listdata[3].append("Image: eco_blacklandprairie.jpg")
    listdata[4].append("Image: eco_crosstimbers.png")
    listdata[5].append("Image: eco_southplains.png")
    listdata[6].append("Image:eco_edwards.png")
    listdata[7].append("Image:eco_rollingplains.jpg")
    listdata[8].append("Image:eco_highplains.png")
    listdata[9].append("Image:eco_transpecos.jpg")
    for lis in listdata:
        for entry in lis:
            if isinstance(entry, list):
                key = entry[0]
                entry.remove(entry[0])
                value = entry;
            else:
                ls = entry.split(':')
                key = ls[0]
                value = ls[1]
            dictionary[key].append(value)
            size = len(dictionary['Ecoregion'])
        for dic in dictionary:
            if len(dictionary[dic]) != size:
                dictionary[dic].append("")
    for i in range(len(listdata)):
        ecoregion = Ecoregions()
        ecoregion.name=dictionary['Ecoregion'][i]
        ecoregion.image=dictionary['Image'][i]
        ecoregion.description=dictionary['Paragraph'][i]
        ecoregion.conifers=dictionary['Conifers'][i]
        ecoregion.grasses=dictionary['Grasses'][i]
        ecoregion.shrubs=dictionary['Shrubs'][i]
        ecoregion.succulent=dictionary['Succulents'][i]
        ecoregion.trees=dictionary['Trees'][i]
        ecoregion.vine=dictionary['Vine'][i]
        ecoregion.vines=dictionary['Vines'][i]
        ecoregion.wildflowers=dictionary['Wildflowers'][i]
        ecoregionlist.append(ecoregion)
    """df = pd.DataFrame(dictionary)
    df.to_csv('./plant_csv_ecoregions.csv')"""
#createEcoRegions()
#with open('ecoregionlist.txt', 'wb') as fp:
 #   pickle.dump(ecoregionlist, fp)
with open('ecoregionlist.txt', 'rb') as fp:
    ecoregionlist=pickle.load(fp)
print()