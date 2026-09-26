cart = [
    ["Bread", 60, 2],
    ["Milk", 120, 1],
    ["Eggs", 15, 12],
]

grand_total = 0
for item in cart:
    name, price, qty = item
    line_total = price * qty
    grand_total += line_total 
    print(f"{name}: Rs. {line_total}")

print(f"Grand total: Rs. {grand_total}")
