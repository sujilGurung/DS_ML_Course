prices = {"tea": 20, "coffee": 50, "samosa": 25}
print("Menu:", prices)

item = input("What do you want? ")
qty  = int(input("How many? "))

price = prices.get(item, 0)
print("Price of one:", price)
print("Total bill  :", price * qty)

prices ["momo"] =  150
print(f"Cheapest: {min(prices.values())}")
print(f"Costliest: {max(prices.values())}")
print(sorted(prices))
print(sorted(prices.items()))
# Your job:
# 1. add "momo": 150 to the menu
# 2. print the cheapest and costliest price
# 3. print item names A-Z with sorted(prices)