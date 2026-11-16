'''
l1=input("Enter name:").split()

print(l1)

print(l1[1])
'''

'''
#using standard method

arr1=[]

n=int(input("Enter Number of Elements: "))

for i in range(0,n):
    e1=input("Enter name: ")
    arr1.append(e1)
print(arr1)

'''
#using numpy

import numpy as np

arr=np.array([9,18,27,36,81,90])
print(arr)

ar=np.zeros(9)
print(ar)

fir=np.arange(9,90,9)
print(fir)

print(np.mean(fir))