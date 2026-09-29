a = {1, 2, 3, 4}
b = {3, 4, 5}

print(a | b)    # {1, 2, 3, 4, 5}   a.union(b)
print(a & b)    # {3, 4}            a.intersection(b)
print(a - b)    # {1, 2}            a.difference(b)
print(b - a)    # {5}
print(a ^ b)    # {1, 2, 5}         a.symmetric_difference()

a |= b          # a is changed now
print(a)        # {1, 2, 3, 4, 5}

small = {1, 2}
big   = {1, 2, 3, 4}

print(small <= big)            # True   subset
print(small.issubset(big))     # True
print(big >= small)            # True   superset
print(big.issuperset(small))   # True

print({1, 2}.isdisjoint({5, 6}))   # True
print({1, 2} == {2, 1})            # True

a = {1, 2}
b = a            # same set, two names
c = a.copy()     # a real copy
a.add(3)
print(b)         # {1, 2, 3}   changed too!
print(c)         # {1, 2}      safe

f = frozenset([1, 2])
f.add(3)         # AttributeError: can't change

votes = ["tea", "coffee", "tea", "tea", "milk"]

unique = set(votes)
print(unique)           # {'tea', 'coffee', 'milk'}
print(len(unique))      # 3
print(sorted(unique))   # ['coffee', 'milk', 'tea']

print(len(votes) != len(unique))   # True: had duplicates


s = {3, 1, 3, 2, 1}
print(len(s))

s.add(4)
print(sorted(s))

print({1, 2} & {2, 3})
print({1, 2} | {2, 3})

s.remove(9)