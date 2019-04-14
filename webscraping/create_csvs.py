import pickle
from webscraping.plant import Plant
from webscraping.park import Parks
from webscraping.ecoregion import Ecoregions
plantlist=[]
parklist=[]
ecoregionlist=[]
with open('ecoregionlist.txt', 'rb') as fp:
    ecoregionlist=pickle.load(fp)
with open('plantlist.txt', 'rb') as fp:
    plantlist=pickle.load(fp)
with open('parklist.txt', 'rb') as fp:
    parklist=pickle.load(fp)
for i in range(len(ecoregionlist)):
    for j in range(len(plantlist)):
        for entry in plantlist[j].ecoregionids:
            if i==0 and entry==0:
                ecoregionlist[i].plantlist.append(j)
            if i == 1 and entry ==1:
                ecoregionlist[i].plantlist.append(j)
            if i == 2 and entry ==2:
                ecoregionlist[i].plantlist.append(j)
            if i == 3 and entry ==3:
                 ecoregionlist[i].plantlist.append(j)
            if i == 4 and entry ==4:
                ecoregionlist[i].plantlist.append(j)
            if i == 5 and entry ==5:
                ecoregionlist[i].plantlist.append(j)
            if i == 6 and entry ==6:
                 ecoregionlist[i].plantlist.append(j)
            if i == 7 and entry ==7:
                ecoregionlist[i].plantlist.append(j)
            if i == 8 and entry ==8:
                ecoregionlist[i].plantlist.append(j)
            if i == 9 and entry ==9:
                ecoregionlist[i].plantlist.append(j)
    ecoregionlist[i].plantlist= list(dict.fromkeys(ecoregionlist[i].plantlist))
    ecoregionlist[i].plantlist.sort()
parklist1=[]
for park in parklist:
    x =Parks()
    x.name = park.name
    x.lat = park.lat
    x.long = park.long
    x.url = park.url
    x.parkplantlist = park.parkplantlist
    x.description = park.description
    x.image = park.image
    x.ecoregion = park.ecoregion
    x.address = park.address
    parklist1.append(x)
for j in range(len(parklist1)):
    entry = parklist1[j].ecoregion.strip()
    if entry == "PINEYWOODS":
        parklist1[j].ecoregionlist.append(0)
    if entry == "GULF PRAIRIES AND MARSHES":
        parklist1[j].ecoregionlist.append(1)
    if entry == "POST OAK SAVANNAH":
        parklist1[j].ecoregionlist.append(2)
    if entry == "BLACKLAND PRAIRIES":
        parklist1[j].ecoregionlist.append(3)
    if entry == "CROSS TIMBERS AND PRAIRIES":
        parklist1[j].ecoregionlist.append(4)
    if entry == "SOUTH TEXAS PLAINS":
        parklist1[j].ecoregionlist.append(5)
    if entry == "EDWARDS PLATEAU":
        parklist1[j].ecoregionlist.append(6)
    if entry == "ROLLING PLAINS":
        parklist1[j].ecoregionlist.append(7)
    if entry == "HIGH PLAINS":
        parklist1[j].ecoregionlist.append(8)
    if entry == "TRANS-PECOS":
        parklist1[j].ecoregionlist.append(9)
with open('ecoregionlist.txt', 'wb') as fp:
    pickle.dump(ecoregionlist, fp)
with open('parklist.txt', 'wb') as fp:
    pickle.dump(parklist1, fp)
Plant.plantcsv(plantlist)
Parks.createcsv(parklist1)
Ecoregions.createcsv(ecoregionlist)