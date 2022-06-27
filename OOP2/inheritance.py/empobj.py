from empit import Empit
from empmkt import EmpMKT
#create object employee IT
mike = Empit('001','Mike',60000)
mike.add_skill('Pythone , Javasrcipt')
mike.add_experience(5)
mike.emp_detail()
mike.it_salary()

#create object employee MKT
anna = EmpMKT('002','Anna','35000')
anna.emp_detail()
anna.mkt_salary()

#พนักงานแผนการตลาดชื่อ Paul มีเงืนเดือน 45000 ได้รับคอมมิสชั่น 35% โดยทำงานอยู่จังหวัดเชียงใหม่
paul = EmpMKT('003','Paul','45000')
paul.add_commission(35)
paul.add_location('Chiang Mai')
paul.emp_detail()
paul.mkt_salary