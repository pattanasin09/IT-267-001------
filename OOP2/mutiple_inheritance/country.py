from geographice import Geographic
from temperature import Temperature

class Country(Geographic,Temperature):
    """def __init__(self,name,area,population) -> None:
        self.name = name
        self.area = area
        self.population = population"""
    def __init__(self,name,area,pop) -> None:
        #super().__init__()
        Geographic.__init__(self)
        Temperature.__init__(self)
        self.name = name
        self.area = area
        self.poppulation = pop
    def getpopulationdensity(self):
        return self.population / self.area
    def show_Deteils(self):
        #ชื่อประเทศ
        print(f'Country : {self.name}')

        #สถานที่ตั้ง latitude และ longitude
        print(f'Location : {self.getcordinate()}')

        #แสดงขนาดพื้นที่,จำนวนประชากร และความหนานแน่น
        print(f'Population : {self.population:,d}')
        print(f'Area : {self.area:,.2f}')
        print(f'Density {self.getpopulationdensity():,.2f}')

        #Time Zone,Climate , Temperature,Weather
        print(f'Time Zone : {self.gettimezone()}')
        print(f'Climate : {self.getclimate()}')
        print(f'Temperature(C) : {self.getcelcisu():.2f}')
        print(f'Temperature(F) : {self.getfahrenheit():.2f}')
        print(f'Weather : {self.getweather()}')

        print('************************')
