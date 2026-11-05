cart = []

for i in range(3):
    name = input("Enter the item name: ")
    q = int(input("Enter the Quantity: "))
    r = int(input("Enter the rate: "))
    
    # Store everything together
    cart.append({
        "name": name,
        "qty": q,
        "total": q * r
    })

# Print everything cleanly
for item in cart:
    print(f"Item: {item['name']}, Quantity: {item['qty']}, Total Bill: {item['total']}")
