from bank import *

class ABank(Bank):
    def __init__(self, bankname: str,loanamount:int,loanyear:int,loanrate:float,interest:float=0,monthlypay:float=0) -> None:
        super().__init__(bankname)
        self.__loanamount = loanamount
        self.__loanyear = loanyear
        self.__loanrate = loanrate
        self.interest = interest
        self.monthlypay = monthlypay
    
    @property
    def loanamount(self):
        return self.__loanamount
    @loanamount.setter
    def loanamount(self,value):
        self.__loanamount = value

    @property 
    def loanyear(self):
        return self.__loanyear
    @loanyear.setter
    def loanyear(self,value):
        self.__loanyear = value
    
    @property
    def loanrate (self):
        return self.__loanrate 
    @loanrate .setter
    def loanrate (self,value):
        self.__loanrate = value
    

    def flat_rate(self):
        return self.loanamount * (self.loanrate /100) * self.loanyear 
    
    
    def flat_rate1(self):
        return (self.loanamount + self.flat_rate()) /24
    def display_interest(self):
        print(f'**** {self.bankname} Loan Info ****')
        print(f'Loan :{self.loanamount:,.2f} baht')
        print(f'Rate:{self.loanrate:.2f}%')
        print(f'Year:{self.loanyear}')
        print('--Interest--')
        print(f'Interest : {self.flat_rate():,.2f} bath')
        print(f'Monthly Repayment : {self.flat_rate1():,.2f} baht')