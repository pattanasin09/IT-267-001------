class JuiceOrder :
    total:float = 0

    def __init__(self,menu:str,size:str='R',) -> None:
        self.menu = menu.upper()
        self.size = size.upper()
        self.price = 0

    def check_menu(self):
        menu_dictionary= {
            "OJ":25,
            "AJ":25,
            "WJ":30,
            "PJ":30,
            }
        if self.menu in menu_dictionary:
            self.price = menu_dictionary.get(self.menu)

    def compute_price(self):
        if self.size == 'L':
            self.price +=5
        else:
            self.price

        JuiceOrder.total = self.price

    def display_detail(self):
        self.check_menu()
        self.compute_price()
        return f'{self.menu}({self.size} * {self.price}) => {JuiceOrder.total} baht'

if __name__=="__main__":

    wj1 = JuiceOrder('WJ','l')
    oj2 = JuiceOrder('oj')
    pj3 = JuiceOrder('pj','l')
    print(wj1.display_detail())
    print(oj2.display_detail())
    print(pj3.display_detail())


