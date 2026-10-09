def make_bill(*prices, discount=0):
    if not prices:
        print("Cart is empty!")
        return 0
    total = sum(prices)
    saved = total * discount / 100
    print(f"Items:     {len(prices)}")
    print(f"Costliest: Rs. {max(prices)}")
    print(f"Total:     Rs. {total}")
    print(f"Discount:  Rs. {round(saved, 2)}")
    return round(total - saved, 2)

pay = make_bill(1200, 350, 140, 260, discount=10)
print(f"To pay:    Rs. {pay}")
no_price = make_bill()
print(f"No prices passes: {no_price}")

user_prices = []


while True:
    price = input("Enter prices (or q to quit): ")
    if price.isdigit():
        user_prices.append(int(price)) 

    elif price == "q":
        print("Thank you!")
        break

    elif not price.isdigit():
        print("Enter price in numbers.")
        break

user_pay = make_bill(*user_prices)
print(user_pay)
