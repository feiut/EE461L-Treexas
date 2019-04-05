class Ecoregions:
    def __init__(self):
        self.name=""
        self.plantlist=[]
        self.stateparklist=[]
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
    @staticmethod
    def createcsv(ecoregionlist):
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
            "Image": [],
            "StateParks": [],
            "Plants": []
        }
        for eco in ecoregionlist:
            dictionary['Ecoregion'].append(eco.name)
            dictionary['Paragraph'].append(eco.description)
            dictionary['Trees'].append(eco.trees)
            dictionary['Shrubs'].append(eco.shrubs)
            dictionary['Succulents'].append(eco.succulent)
            dictionary['Vines'].append(eco.vines)
            dictionary['Vine'].append(eco.vine)
            dictionary['Conifers'].append(eco.conifers)
            dictionary['Grasses'].append(eco.grasses)
            dictionary['Wildflowers'].append(eco.wildflowers)
            dictionary['Image'].append(eco.image)
            dictionary['StateParks'].append(eco.stateparklist)
            dictionary['Plants'].append(eco.plantlist)
        df = pd.DataFrame(dictionary)
        df.to_csv('./plant_csv_ecoregions.csv')