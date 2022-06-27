#ถ้าเป็น + เพิ่มปกติ #ใส่ _ หน้าชื่อ -  ใส่_ 2 ครั้งหน้าชื่อ
class Employee:
    def __init__(self,id,name,salary) -> None:
        self.name = name
        self.id = id
        self._salary = salary

    def emp_detail(self):
        print(f'Id = {self.id}')
        print(f'Name = {self.name}')

    def _emp_salary(self):
        print(f'salary : {self._salary}')