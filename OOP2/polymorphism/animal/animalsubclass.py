from re import L
from animal import Animal

class Dog(Animal):
    def info(self):
        #return super().info()
        Animal.info(self) # -- Animal Information
        print('I am a dog .')
        print(f'My name is {self.name}')
        print(f'I am {self.age} year old.')
    
    def make_sound(self):
        #return super().make_sound()
        Animal.make_sound(self)# === Animal Sound ===
        print(f'Hey I make Woof!! Woof!! sound. ')
    
class Cat(Animal):
    def info(self):
        #return super().info()
        Animal.info(self) # -- Animal Information
        print('I am a cat .')
        print(f'My name is {self.name}')
        print(f'I am {self.age} year old.')
    
    def make_sound(self):
        #return super().make_sound()
        Animal.make_sound(self)# === Animal Sound ===
        print(f'Hey I make Meaw!! Meaw!! sound. ')

class Cow(Animal):
    def info(self):
        #return super().info()
        Animal.info(self) # -- Animal Information
        print('I am a cow .')
        print(f'My name is {self.name}')
        print(f'I am {self.age} year old.')
    
    def make_sound(self):
        #return super().make_sound()
        Animal.make_sound(self)# === Animal Sound ===
        print(f'Hey I make Moo!! Moo!! sound. ')