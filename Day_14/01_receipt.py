def receipt(func):
    def wrapper(*args, **kwargs):
        print("=" * 24)
        print("      MOMO HOUSE")
        print("=" * 24)
        result = func(*args, **kwargs)
        print("-" * 24)
        print("Thank you! Visit again")
        return result
    return wrapper


def discount(func):
    def wrapper(*args, **kwargs):
        print("-" * 5, "The Total", "-" *5)
        result = func(*args, **kwargs)
        return round(result * 0.9, 2)
    return wrapper


@receipt
def order(item, qty, price):
    total = qty * price
    print(f"{item} x {qty} = Rs. {total}")
    return total


@receipt
def pay(amount):
    print(f"Paid Rs. {amount}")


@discount
def final_price(total):
    print(f"The total Rs.{total}")
    return total


bill = order("Chicken momo", 2, 180)
print("Saved bill:", bill)

pay(bill)

print("After 10% discount:", final_price(bill))