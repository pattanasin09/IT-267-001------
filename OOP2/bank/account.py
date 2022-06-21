class Account:
    
    def __init__(self) -> None:
        self.acctype = ''
        self.number = ''
        self.balance = 0
        self.accname = ''

    def open_account(self,accname:str,acctype,accno,balance:int=100):
        self.accname = accname
        self.acctype = acctype
        self.accno = accno
        self.balance = balance
    
    def display_balance(self):
        return f'{self.accname} account balance  = {self.balance} bath'