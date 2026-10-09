menu = {"momo": 150, "chowmein": 120, "tea": 30, "lassi": 80}
insert_item = input("Enter items: ").lower().split()
def place_order(customer, *items, **options):
    print(f"Order for {customer}")
    total = 0
    for num, item in enumerate(items, start=1):
        if item in menu:
            print(f"{num}. {item}: Rs. {menu[item]}")
            total += menu[item]
        else:
            print(f"{num}. {item}: not on the menu")

    if options.get("delivery"):
        print("Delivery: Rs. 50")
        total += 50
    for key, value in options.items():
        if key != "delivery":
            print(f"Note: {key} = {value}")

    print(f"Total: Rs. {total}")
    return total

total = place_order("You", *insert_item, delivery=True, spicy="extra")

vat_total = round(total * 1.13, 2)
print(f"Grand Total with 13% VAT. {vat_total}")
