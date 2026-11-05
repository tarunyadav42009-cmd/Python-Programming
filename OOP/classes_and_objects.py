'''
With Parameter:

class calc:
    def num(self,n1,n2):
        self.no1=n1
        self.no2=n2

    def add(self):
        Add=self.no1+self.no2
        print("Addition = ",Add)

c1=calc()
c1.num(3,5)
c1.add()

'''

class calc:
    def get_data(self):
        self.no1=int(input("Enter first number : "))
        self.no2=int(input("Enter second number : "))
        
    def add(self):
        Add=self.no1+self.no2
        print("Adition: ",Add)

c1=calc()
c1.get_data()
c1.add()