'''
list 
to print all the records 
to print record in range wise 
replace the value 
delete  the value 
find the length of list 
find max value from list , min
add record in list index wise 
add record to the last 
count the total value in list
find the index value of particular record
give the pop example
reverse the list 
copy from one list to ano
'''
TSG=[31,13,445,657,78]
print(TSG)

TSG.insert(3,34)
print(TSG)

TSG[0]=45
print(TSG)

del TSG [3]
print(TSG)

print("Max Value:",max(TSG))

print("Minimum Value:",min(TSG))

TSG.insert(3,90)
print("After inserting a value to list:",TSG)

TSG.append(87)
print("After appending a value to the list:",TSG)

print("Length of list:",len(TSG))

print("Value at Index 2:",TSG[2])

TSG.pop(2)
print("After removing the value from TSG:",TSG)

TSG.reverse()
print("After Reversing the List:",TSG)
