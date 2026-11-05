#__init__ is a constructor name
'''
class car:
    def __init__(self):
        self.a1="unknown"
        self.a2=90
        print("This is constructor")

    def display(self):
        print("This is not without parameter")

c1=car()
c1.display()
'''

'''
class F1:
    def __init__(self,F1car,year):
        self.m1=F1car
        self.y1=year

    def Super(self):
        print("model is :",self.m1)
        print("Year is :",self.y1)

c2=F1("Mercedes",2025)
c2.Super()
'''

'''
class student:
    count=0
    def __init__(self):
        student.count=student.count+1

s1=student()
s2=student()
print("The number of student ", student.count)
'''

class student:
    count=0
    def __init__(self):
       print("This is first constructor!")
    def __init__(self):
           print("This is second constructor!")

s1=student()
