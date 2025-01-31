class city:
    def __init__(self,cityName,regionName,countryName,numOfCitizens,zipCode,areaCode):
        self.cityName = cityName
        self.regionName = regionName
        self.countryName = countryName
        self.numOfCitizens = numOfCitizens
        self.zipCode = zipCode
        self.areaCode = areaCode
    def fullAdress(self):
        return (f" City Name :{self.cityName}, Region Name :{self.regionName}, Country Name :{self.countryName}, ZIP: {self.zipCode}, Area Code: {self.areaCode}")


bratislava =city('Bratislava','Bratislavsky','Slovensko','442306','81101','+42102')

print(bratislava.fullAdress())