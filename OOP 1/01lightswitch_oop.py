class LightSwitch():
    def _init_(self) -> None:
        self.switch_status = False

    def turnon(self):
        self.switch_status = True
    
    def turnoff(self):
        self.switch_status = False

    def show(self):
        print(f"status = {self.switch_status}")

#สร้างวัตถุ (object) จากแม่พิมพ์ (Class)
switch_object = LightSwitch() #switch_object ถูกสร้างมาจาก class LightSwitch
#และแต่ละ object สามารถแตกต่างกันได้

#เรียกใช้เมธอด / ฟังก์ชั่น #เรียกใช้ชื่อ object
switch_object.show()#Fales
switch_object.turnon()
switch_object.show()#True
switch_object.turnoff()
switch_object.show()#Fales
switch_object.turnoff()
switch_object.show()#Fales
