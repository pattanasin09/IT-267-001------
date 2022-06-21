#this file is inside bank package
#call module
from customer import Customer
from account import Account

cus1 = Customer()
cus1.new_customer()
print(cus1.name)

cus1_acc = Account
cus1_acc.open_account('ttff','Saving','10-123-456',500)

print('**** Open Bank Account Detail ****')
print(cus1.cus_info())
print(cus1_acc.display_balance())
#print(cus1.cus_info())
