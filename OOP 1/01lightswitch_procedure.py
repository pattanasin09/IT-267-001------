#สร้างฟังก์ชั้น เปิด และ ปิดไฟ
def turnon():
    global  switch_status
    switch_status = True #เปลี่ยนสถานะเป็นเปิดไฟ
    
def turnoff():
    global  switch_status
    switch_status = False #เปลี่ยนสถานะเป็นปิด
    
switch_status = False #

print(f"Status = {switch_status}")
turnon()
print(f"Status = {switch_status}")
turnoff()
print(f"Status = {switch_status}")
turnoff()
print(f"Status = {switch_status}")

 