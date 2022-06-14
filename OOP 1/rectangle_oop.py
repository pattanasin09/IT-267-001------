class Rectangle :
    def __init__(self,width,length) -> None:
        self.width = width
        self.length = length
        self.area = 0

    def get_data(self):
        pass

    def compute_area(self):
        self.area = self.width * self.length

    def print_area(self):
        print(f'Rectangle Area :{self.area}')

# create object
rec_obj = Rectangle(2,5)
rec_obj.compute_area()
rec_obj.print_area()