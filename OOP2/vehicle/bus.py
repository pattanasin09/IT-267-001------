from vehice import Vehice
class Bus(Vehice):
    def __init__(self, name, wheels, maxspeed, vin) -> None:
        super().__init__(name, wheels, maxspeed, vin)
    
    def set_colour(self,color):
        self.color = color

    def set_capacity(self,capacity):
        self.capacity = capacity

    def bus_detail(self):
        self.v_detail()
        print(f'color : {self.color}')
        print(f'capacity : {self.capacity}')
        

