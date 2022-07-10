
from donkey import *
from horse import *

class Mule(Horse,Donkey):
    def __init__(self, name: str, color: str,age:int,weight:float,max_height: float = 200) -> None:
        super().__init__(name, color, max_height,)
        self.age = age
        self.weight = weight
        
    
    def run(self):
        super().run()
    
    def show_info(self):
        print(f'Color :{self.color}')
        print(f'Max Height :{self.max_height} cm')
        print(f'Age :{self.age}-year-old')
        print(f'Weight :{self.weight} kg')

mule1 =Mule('Mumu','Blue-eyed cream',3,200)
print(f'**** Mumu Info ****')
mule1.show_name()
mule1.show_info()

mule2 = Mule('Meme','Palomino',1,120.7)
print(f'**** Meme Info ****')
mule2.sound()
mule2.show_name()
mule2.show_info()






    
    