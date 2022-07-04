from vehicle_abstract import Venicle

class Car(Venicle):
    def __init__(self, brand, speed) -> None:
        #super().__init__(brand, speed)
        Venicle.__init__(self,brand,speed)
        self.__year = 0
        self.__maintanance = 0
    
    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self,value):
        self.__year = value
    
    @property
    def maintanance (self):
        return self.__maintanance 
    @year.setter
    def maintanance(self,value):
        self.__maintanance  = value
    
    #implement abstact method
    def show_detail(self):
        super().show_detail()
        print('====== Car Detail =====')
        print(f'{self.brand} with speed {self.speed} km/hr')
        print(f'manufactered in {self.year} has')
        print(f'{self.gear} gear and {self.seat} seats')
    
    #implement Car method
    def show_maintanance(self):
        print('--- Car Maintanance ---')
        print(f'The lastest maintance in {self.maintanance}')
    
    
class Truck(Venicle):
    def __init__(self, brand, speed) -> None:
        super().__init__(brand, speed)
        self.__capacity = 100
        self.__whell = 4

    @property
    def capacity(self):
        return self.__capacity
    @capacity.setter
    def capacity(self,value):
        self.__capacity = value
    
    @property
    def whell(self):
        return self.__whell
    @whell.setter
    def whell(self,value):
        self.__whell = value
    
    def show_detail(self):
        super().show_detail()
        print('====== Truck Detail =====')
        print(f'{self.brand} with speed {self.speed} km/hr')
        print(f'carry {self.capacity} tons')
    
    def show_price(self):
        print('++++ Truck price ++++')
        if self.whell == 4:
            price = 1000
        elif self.whell == 6:
            price = 1500
        elif self.whell == 8:
            price = 2000
        else :
            price = 3000
        print(f'{self.whell}Truck = {price} bath/day .')

class Motocycle(Venicle):
    def __init__(self, brand, speed) -> None:
        super().__init__(brand, speed)
        self.__cc = 150
        self.__model = None
    
    @property
    def cc(self):
        return self.__cc
    @cc.setter
    def cc(self,value):
        self.__cc = value
    
    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self,value):
        self.__model = value
    
    def show_detail(self):
        super().show_detail()
        print('====== Motocycle Detail =====')
        print(f'{self.brand} with speed {self.speed} km/hr')
        print(f'cc {self.cc}')
    
    