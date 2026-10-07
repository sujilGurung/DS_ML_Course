'''
Create 02_shopping_bill.py. Two lists: items and prices.
 show_bill() walks them together with zip(). bill_total() 
 uses sum() and round(), with a default discount of 0, like Day 09.
'''


def show_bill(items, prices):
    
    for num, (item, price) in enumerate(zip(items, prices), start=1):
        print(f"{num}.{item}: Rs.{price}")
    cheapest = min(prices)
    cheap = items[prices.index(cheapest)]
    print(f"Cheap item is {cheap} Rs.{cheapest} ")
    
    #     if minimum >= price:
    #         minimum = price
    #          = items
    # print(f"Minimum price item is {item} Rs.{minimum}")


def bill_total(items, discount=0):
    total = sum(prices)
    return round(total - total*discount / 100, 2)

def index(items):
    for num, items in enumerate(items, start=1):
        print(f"{num}. {items}")


items = ["ball", "t-shirt", "pant" ]
prices = [1000, 2000, 2300]

show_bill(items, prices)
print(f"Items: {len(items)}")
print(f"Costliest: Rs. {max(prices)}")
print(f"Total: Rs. {bill_total(prices)}")
print(f"After 10% off: Rs. {bill_total(prices, 10)}")
print(index(items))





    