#Show the menu dictionary. Ask for an item. If it's on the menu, ask how many and print the total.
#  If not, say sorry. Then give a discount with if

menu = {
    "tea": 130,
    "coffee": 200,
    "chowmeen":200
    }

item = input("Enter menu item: ")
if item in menu:
    price = menu[item]
    quantity = int(input("Enter the quantity of item: "))
    discount = 0
    total = quantity * price
    if total >= 500:
        discount = int(0.10 * total)
    elif total >= 200:
        discount = int(0.05 * total)
    else:
        print("Sorry there is no discount for your total")

    final_price = total - discount
    print(f"Your Grand total of {quantity} {item} is {final_price} discounted price: {discount}")
    
else:
    print("Sorry! item unavailable")