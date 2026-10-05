
def remove_duplicates(items):
    return sorted(set(items))

def total_price(cart):
    total = 0
    for price in cart.values():
        total += price
    return total
def common(a, b):
    return list(set(a) & set(b))
def costliest(cart):
    return max(cart, key=cart.get)

names = ["Ram", "Sita", "Ram", "Hari", "Sita"]
print(remove_duplicates(names))   # ['Hari', 'Ram', 'Sita']

cart = {"rice": 1200, "oil": 350, "sugar": 140}
print(total_price(cart))          # 1690

print(common([1, 2, 3], [2, 3, 4]))  # [2, 3]
print(costliest(cart))  # rice
# Your job:
# 1. write common(a, b): items in both lists
#    (hint: set(a) & set(b) from Day 05)
# 2. write costliest(cart): return the costliest item's name