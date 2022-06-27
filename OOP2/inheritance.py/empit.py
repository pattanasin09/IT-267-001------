from employee import Employee
class Empit(Employee):
    def __init__(self, id, name, salary) -> None:
        super().__init__(id, name, salary)
        self.skill = None
        self.experience = None
        self.department = 'IT'

    def add_skill(self,skill:str):
        self.skill = skill

    def add_experience(self,experience:int):
        self.experience = experience

    def emp_detail(self):
        print('***** Employee IT Detail *****')
        #เรียกใช้เมธอท emp_detail ของคลาส Exployee เพื่อสแดง id,name
        super().emp_detail() # super คืออิงมาจาก class แม่
        print(f'skill : {self.skill}')
        print(f'experience : {self.experience} year(s)')
        
    def it_salary(self):
        self._emp_salary()

