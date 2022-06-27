class Project:
    def __init__(self,name,time,location,) -> None:
        self.name = name
        self.time = time
        self._locatin = location
        self.__budget = 50

    def show(self):
        print('======= Project Detail =======')
        print(f'Name : {self.name}')
        print(f'Time : {self.time} months')
        print(f'Location : {self._locatin}')

    def get_budget(self):
        return self.__budget

    def update_budget(self,budget):
        self.__budget = budget
