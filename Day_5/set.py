nums = {1, 2, 2, 3, 3, 3}
print(nums)            # {1, 2, 3}   duplicates gone

colors = {"red", "blue"}

print(set([1, 1, 2]))  # {1, 2}   list to set
print(set("aab"))      # {'a', 'b'}  any order

empty = set()          # the right way
wrong = {}
print(type(wrong))     # <class 'dict'>   not a set!

colors = {"red", "blue", "green"}
print(colors)       # order may be different!

print(colors[0])
# TypeError: 'set' object is not subscriptable

ok  = {1, "hi", (2, 3)}    # numbers, strings, tuples
bad = {1, [2, 3]}
# TypeError: unhashable type: 'list'

colors = {"red", "blue"}

colors.add("green")              # add one item
colors.add("red")                # already there: no change
colors.update(["pink", "gold"])  # add many items

colors.remove("pink")     # remove (error if missing)
colors.discard("black")   # remove (never an error)
colors.pop()              # remove a random item
colors.clear()            # empty it: set()
del colors                # delete the whole set

nums = {4, 9, 1, 7}

print(9 in nums)        # True
print(5 not in nums)    # True
print(len(nums))        # 4
print(max(nums))        # 9
print(min(nums))        # 1
print(sum(nums))        # 21
print(sorted(nums))     # [1, 4, 7, 9]   a list