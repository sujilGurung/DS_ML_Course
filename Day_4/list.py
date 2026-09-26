list = [1,3,4,5,6,7,5,3,3,1,10]
list2 = list.copy() #new values copied
list2.insert(1,12)
print(list2)

list = [1,3,4,5,6,7,5,3,3,1,10]
list2 = list        #address variable values.
list2.append(32)
print(list)
list2.sort()
print(list2)
list2.sort(reverse="True")
print(list2)
print(sum(list2))
print(min(list2))
print(max(list2))
print(len(list2))
list2.remove(10)
print(list2)
list2.pop()
print(list2)
e = sorted(list2)
print(e)

print(list2)