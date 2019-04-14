import pickle
from webscraping.plant import Plant
plantlist=[]
with open('plantlist.txt','rb') as fp:
    plantlist=pickle.load(fp)
i=0
for plant in plantlist:
    plant.ecoregionids= []
    if i<470:
        lowerzone = -1
        higherzone= -1
        water =  -1
        if len(plant.zones)==2:
            if len(plant.zones[0])==1:
                lowerzone = int(plant.zones[0])
            else:
                lowerzone = int(plant.zones[0][:-1])
            if len(plant.zones[1]) == 1:
                higherzone = int(plant.zones[1])
            else:
                higherzone = int(plant.zones[1][:-1])
        elif len(plant.zones)==1:
            if len(plant.zones[0]) == 1:
                lowerzone = int(plant.zones[0])
            else:
                lowerzone = int(plant.zones[0][:-1])
            higherzone=15
        if lowerzone>higherzone:
            j = lowerzone
            lowerzone = higherzone
            higherzone=lowerzone
        waterzone = plant.waterdemand.split(',')
        if len(waterzone)==2:
            if waterzone[0].strip().lower()=="medium":
                water= 1
            else:
                water=3
        else:
            input = waterzone[0].strip().lower()
            if input == "very low":
                water=5
            elif input == "low":
                water=4
            elif input == "high":
                water =0
            elif input == "medium":
                water =2
        if lowerzone == -1 and higherzone == -1:
            if water == 0:
                plant.ecoregionids.append(0)
                plant.ecoregionids.append(1)
            elif water ==1:
                plant.ecoregionids.append(0)
                plant.ecoregionids.append(1)
                plant.ecoregionids.append(2)
                plant.ecoregionids.append(3)
            elif water ==2:
                plant.ecoregionids.append(0)
                plant.ecoregionids.append(1)
                plant.ecoregionids.append(2)
                plant.ecoregionids.append(3)
                plant.ecoregionids.append(4)
                plant.ecoregionids.append(5)
            elif water ==3:
                plant.ecoregionids.append(0)
                plant.ecoregionids.append(1)
                plant.ecoregionids.append(2)
                plant.ecoregionids.append(3)
                plant.ecoregionids.append(4)
                plant.ecoregionids.append(5)
                plant.ecoregionids.append(6)
                plant.ecoregionids.append(7)
            elif water ==4:
                plant.ecoregionids.append(0)
                plant.ecoregionids.append(1)
                plant.ecoregionids.append(2)
                plant.ecoregionids.append(3)
                plant.ecoregionids.append(4)
                plant.ecoregionids.append(5)
                plant.ecoregionids.append(6)
                plant.ecoregionids.append(7)
                plant.ecoregionids.append(8)
            elif water ==5:
                plant.ecoregionids.append(0)
                plant.ecoregionids.append(1)
                plant.ecoregionids.append(2)
                plant.ecoregionids.append(3)
                plant.ecoregionids.append(4)
                plant.ecoregionids.append(5)
                plant.ecoregionids.append(6)
                plant.ecoregionids.append(7)
                plant.ecoregionids.append(8)
                plant.ecoregionids.append(9)
        else:
            if lowerzone<=6 and higherzone>=6 and (water==3 or water==4 or water==5):
                plant.ecoregionids.append(7)
                if water != 3:
                    plant.ecoregionids.append(8)
            if lowerzone<=7 and higherzone>=7 and (water==3 or water==4 or water==5):
                plant.ecoregionids.append(6)
                plant.ecoregionids.append(7)
                if water != 3:
                    plant.ecoregionids.append(8)
            if lowerzone <= 8 and higherzone >= 8:
                if water == 0:
                    plant.ecoregionids.append(0)
                if water == 1:
                    plant.ecoregionids.append(0)
                    plant.ecoregionids.append(2)
                    plant.ecoregionids.append(3)
                if water == 2:
                    plant.ecoregionids.append(0)
                    plant.ecoregionids.append(2)
                    plant.ecoregionids.append(3)
                    plant.ecoregionids.append(4)
                if water == 3 or water ==4:
                    plant.ecoregionids.append(0)
                    plant.ecoregionids.append(2)
                    plant.ecoregionids.append(3)
                    plant.ecoregionids.append(4)
                    plant.ecoregionids.append(6)
                if water == 5:
                    plant.ecoregionids.append(0)
                    plant.ecoregionids.append(2)
                    plant.ecoregionids.append(3)
                    plant.ecoregionids.append(4)
                    plant.ecoregionids.append(6)
                    plant.ecoregionids.append(9)
            if lowerzone <= 9 and higherzone >= 9:
                if water == 0:
                    plant.ecoregionids.append(1)
                if water == 1:
                    plant.ecoregionids.append(1)
                    plant.ecoregionids.append(2)
                    plant.ecoregionids.append(3)
                if water >= 2:
                    plant.ecoregionids.append(1)
                    plant.ecoregionids.append(2)
                    plant.ecoregionids.append(3)
                    plant.ecoregionids.append(5)
    i=i+1
    plantregion=plant.econregion
    if plantregion != "N/A":
        plantreg=plantregion.split(',')
        for entry in plantreg:
            entry=entry.strip()
            if entry=="PINEYWOODS":
                plant.ecoregionids.append(0)
            if entry =="GULF PRAIRIES AND MARSHES":
                plant.ecoregionids.append(1)
            if entry =="POST OAK SAVANNAH":
                plant.ecoregionids.append(2)
            if entry =="BLACKLAND PRAIRIES":
                plant.ecoregionids.append(3)
            if entry =="CROSS TIMBERS AND PRAIRIES":
                plant.ecoregionids.append(4)
            if entry =="SOUTH TEXAS PLAINS":
                plant.ecoregionids.append(5)
            if entry =="EDWARDS PLATEAU":
                plant.ecoregionids.append(6)
            if entry =="ROLLING PLAINS":
                plant.ecoregionids.append(7)
            if entry =="HIGH PLAINS":
                plant.ecoregionids.append(8)
            if entry =="TRANS-PECOS":
                plant.ecoregionids.append(9)
    plant.ecoregionids=list(dict.fromkeys(plant.ecoregionids))
    plant.ecoregionids.sort()
with open('plantlist.txt','wb') as fp:
    pickle.dump(plantlist,fp)
Plant.plantcsv(plantlist)