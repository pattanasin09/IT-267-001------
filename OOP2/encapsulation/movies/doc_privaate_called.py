from documentary_private import Documentary
m = Documentary('Mulan',2020,'action')
#m.__get__movie()#เรียก private method ไม้ได้
#print(m._genre)# เรียก private attribute ไม่ได้
m.print_detail()
print(f'year : {m._Movie__year}')
