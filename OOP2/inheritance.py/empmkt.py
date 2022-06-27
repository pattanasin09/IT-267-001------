from employee import Employee
class EmpMKT(Employee):
    def __init__(self, id, name, salary) -> None:
        super().__init__(id, name, salary)
        self.location = 'Bangkok'
        self.commision = '30'
        self.departmaent = 'Marketting'
    
    def add_location(self,location):
        self.location = location
    
    def add_commission(self,commission):
        self.commision = commission

    def emp_detail(self):
        print('***** Employee MKT Detail *****')
        super().emp_detail()
        print(f'location : {self.location}')
        print(f'commision : {self.commision} %')
    
    def mkt_salary(self):
        self._emp_salary()