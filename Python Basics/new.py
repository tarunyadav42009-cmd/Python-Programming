'''
Write a Python program to create class rectangle with data
members length and breadth. Create suitable methods for reading
and printing area and perimeter of rectangle.


'''

class rectangle: 
            def Area(Self):
                length=int(input("Enter Length:"))
                breadth=int(input("Enter Breadth:"))  
                area_rectangle=length*breadth
                perimeter=2*(length+breadth)
                print("The area of rectangle is",area_rectangle)
                print("The perimeter of rectangle is",perimeter)

K=rectangle()
K.Area()