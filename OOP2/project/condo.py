from project import Project
class Condo(Project):
    def __init__(self, name, time, location, budget,type) -> None:
        super().__init__(name, time, location)
        self.__budget = budget #condo ' s instance variable
        self.type = 'Condo'
    
    def show(self):
        super().show()
        print(f'Type : {self.type}')
        print(f'Condo Budger : {self.__budget} MB')
        print(f'Project budget : {self.get_budget()} MB')  