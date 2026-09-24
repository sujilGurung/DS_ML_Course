item = input("Enter an item: ")
price = int(input("Enter price of item: "))
quantity = int(input("Enter item quantity: "))
total = price*quantity
tax = 0.13
tax_rate = total*tax
final_price = total+tax_rate
print(f"Your {item} of {quantity}quantity Gross price is {final_price} after 13% tax")
