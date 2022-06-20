bird_typr = 'parrot'

class Bird:
    #class variable
    brid_name = 'Peter'

    def __init__(self,color) -> None:
        #instance variable 
        self.color = color

        #local variable
        country = 'Thailand'
        print(country)
    
    def show(self):
        return f'{bird_typr}{Bird.brid_name} has {self.color}  '

if __name__ == '__main__':
    print(f'*****{bird_typr}******') #เรียกใช้ global variable
    my_bird = Bird('Red,Yellow')
    print(my_bird.show())

    #เรียก class variable
    #print(bird_name) เกิด error
    
    #เรียก class variable ชื่อคลาส.variable
    print(Bird.brid_name)
    #ชื่อวัตถุ .class_variable
    print(my_bird.brid_name)

    #เรียก instance variable
    #print(Bird.color)#error

    #ชื่อวัตถุ.instance variable
    print(my_bird.color)