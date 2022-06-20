import cafe 
#แสดงรายการขนมของร้าน
dessert_menu = cafe.Dessert()
print(dessert_menu.show_dessert())

#แสดงรายการเครื่องดื่ม
drink_menu = cafe.Drink()
print(drink_menu.show_drink())

#เพิ่มรายดารเครื่องดื่ม
drink_menu.add_drink('juice')
drink_menu.add_drink('smoothy')
print(drink_menu.show_drink())