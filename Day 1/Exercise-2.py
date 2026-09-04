# Make a shopping cart program

item = input("What item you want to buy:")
price = float(input("Enter the price :"))
quantity= int (input ("Enter the quantity :"))

total = price * quantity 

print(f"\nSo your total bill is: {total} $")
print(f"You bought {quantity} {item}(s)\n")
print ("Thank you for choosing us!")