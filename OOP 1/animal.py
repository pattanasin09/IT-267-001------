class Animal:
    #Class varabile
    animal = 'CAT'

    def new_animal(self,name:str,breed:str,colour:str,age:int):
        self.name = name
        self.breed = breed
        self.colour = colour
        self.age = age

    
    def print_detail(self):
        print(f'**********')
        print(f'Name: {self.name}')
        print(f'Animal: {self.animal}')
        print(f'Breed: {self.breed}')
        print(f'Coloure: {self.colour}')
        print(f'Age: {self.age}')

    def __del__(self):
        print(f'Object was destroied')

#create object
if __name__== "__main__":
    Animal.animal = "FISH"
    ula = Animal()
    ula.new_animal("Ula","Scottish","White",1)
    ula.animal = "DOG"
    ula.print_detail()

    drac = Animal()
    drac.new_animal("Drac","Scottish","White",1)
    drac.print_detail()
    drac.breed = "Catfish"
    drac.print_detail()

    #เรียกดูข้อมูลของ object ผ่านทางชื่อ class
    Animal.print_detail(ula)#ula.prinnt_detail()
    Animal.print_detail(drac)#drac.prinnt_detail()

    #เรียกดู Class variable ทั้งหมด
    print(f'{Animal.__dict__}')


    #เรียกดู Instance variable ทั้งหมด
    print(f'{ula.__dict__}')

    peter = Animal()

    peter.new_animal('Peter','Parrot','Red Green Yellow ',2)
    # add new attribute to peter 
    peter.lags = 2
    print(f'{peter.__dict__}')