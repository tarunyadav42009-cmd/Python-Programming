# Accept and convert user inputs from string to integers
no1 = int(input("Enter the 1st number: "))
no2 = int(input("Enter the 2nd number: "))

# Addition using augmented assignment (no1 = no1 + no2)
no1 += no2 
print("Addition is ", no1)

# Subtraction (Note: no1 value is now the result of the previous addition)
no1 -= no2 
print("Subtraction is", no1)

# Multiplication
no1 *= no2 
print("Multiplication is", no1)

# Floating-point division (returns a decimal value)
no1 /= no2 
print("Division is", no1)

# Floor division (divides and rounds down to the nearest whole number)
no1 //= no2 
print("Floor Division is", no1)

# Exponentiation (raises no1 to the power of no2)
no1 **= no2 
print("Exponent is", no1)

# Modulo (calculates the remainder of the division)
no1 %= no2 
print("Remainder is", no1)
