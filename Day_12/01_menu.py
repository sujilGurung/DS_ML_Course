'''10 minutes
Create 01_menu.py. The menu is a Day 06 dictionary. 
Sort it by price, find cheap items with filter(), raise every price with map(), 
and find the costliest item with max().'''

menu = {"momo": 150, "chowmein": 120, "tea": 30,
        "lassi": 80, "pizza": 450}

total = sum(menu.values())
print(f"Total of menu prices: {total}")
print("--- Cheapest first ---")
for item, price in sorted(menu.items(), key=lambda x: x[1]):
    print(f"{item}: Rs. {price}")

cheap = list(filter(lambda item: menu[item] < 100, menu))
print("Under Rs. 100:", cheap)

new_prices = list(map(lambda p: p + 10, menu.values()))
print("New prices:", new_prices)

costliest = max(menu, key=lambda item: menu[item])
print("Costliest:", costliest)

budget = int(input("Enter the budget: "))
price_range = list(filter(lambda item: menu[item] <= budget, menu))  
print(f"Your budget items are: {price_range}")
# --- Cheapest first ---
# tea: Rs. 30
# lassi: Rs. 80
# chowmein: Rs. 120
# momo: Rs. 150
# pizza: Rs. 450
# Under Rs. 100: ['tea', 'lassi']
# New prices: [160, 130, 40, 90, 460]
# Costliest: pizza

# Your job:
# 1. print the total of all prices with sum()
# 2. ask the user for a budget with int(input())
#    and show only the items they can buy