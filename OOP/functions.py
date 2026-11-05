'''
class car:
    def a(self,modolename,year):
        self.m1=modolename
        self.y1=year

    def b(self):
        print("model is :",self.m1)
        print("Year is :",self.y1)

c=car()
c.a("Bugatti Bolide",2025)
c.b()
'''
class calc:
    def a(self,n1,n2):
        self.a=n1
        self.b=n2

    def add(self):
        print(self.a + self.b)

c=calc()
c.a(10,20)
c.add()