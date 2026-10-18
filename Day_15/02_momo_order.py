menu = {"veg momo": 120, "chicken momo": 180, "chowmein": 150}
total = 0

print("=== MOMO HOUSE ===")
for item, price in menu.items():
    print(f"- {item}: Rs. {price}")
orders = []
while True:
    item = input("Item (or done): ").strip().lower()
    if item == "done":
        break
    try:
        price = menu[item]
        
        try:
            qty = int(input("How many? "))
        except ValueError:
            raise ValueError("Quantity must be a number.")

        if qty <= 0:
            raise ValueError("Quantity must be more than 0")
    except KeyError:
        print("Sorry, we don't have", item)
    except ValueError as e:
        print(e)
    else:
        total += price * qty
        print(f"Added {qty} x {item}")
        orders.append((item, qty, total))
print("Total bill: Rs.", total)
print("Your orders:", orders)

# Item (or done): pizza
# Sorry, we don't have pizza
# Item (or done): veg momo
# How many? two
# Quantity must be a number.
# Item (or done): veg momo
# How many? 2
# Added 2 x veg momo
# Item (or done): done
# Total bill: Rs. 240

# Your job:
# 1. if qty is 0 or less, raise ValueError("Quantity
#    must be more than 0"), and print e in except
# 2. save each order in a list and print it at the end