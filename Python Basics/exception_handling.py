"""
a=int(input("Enter first number: "))
b=int(input("Enter Second Number: "))


try:
    c=a/b
    print(c)

except ZeroDivisionError:
    print("Division by zero")

"""

"""
x=23

if x<0:
    raise Exception("Sorry! no negative numbers allowed!")

"""

"""
list=[1,2,3] 

try:
    a=list[1]
    print(a)

except  IndexError:
    print("Out of range")
"""

"""
a=int("abc")

print(a)
"""

"""

try:
    a=int("abc")
    
except ValueError as e:
    print(e)

"""

"""
try:
    a=int("abc")

except ValueError:
    print("Value Error!!!")
"""

"""
try:
    result="hello"+5
except TypeError as e:
    print(e)

"""

my_list = [1, 2, 3]

for i in range(len(my_list)):
    print(my_list[i])

try:
    print(my_list[3])
except IndexError:
    print("Index out of range!")
