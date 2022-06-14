class Daigram :

    def study(self,id:str,name:str,major:str) :
        self.id = id
        self.name = name
        self.major = major
        
    def dispay_deteil(self):
        print(f'**********')
        print(f'Id: {self.id}')
        print(f'Name: {self.name}')
        print(f'major: {self.major}')

    def __del__(self):
        print(f'Object Destroyed')

if __name__ == "__main__":
    jess = Daigram()
    jess.study(111,"Jessical",'IT')
    jess.dispay_deteil()

    john = Daigram()
    john.study(112,"John","MKT")
    john.dispay_deteil()
    


