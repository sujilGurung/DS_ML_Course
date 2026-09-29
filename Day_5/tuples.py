fruits = ("apple", "banana", "cherry")
info   = ("Ram", 20, True)       # mixed types are OK
empty  = ()                      # empty tuple

nums = 1, 2, 3                   # brackets are optional
print(nums)                      # (1, 2, 3)

one = ("apple",)                 # one item: add a comma!
not_tuple = ("apple")            # this is just a string

print(tuple([1, 2]))             # (1, 2)
print(type(fruits))              # <class 'tuple'>

days = ("Sun", "Mon", "Tue", "Wed", "Thu")

print(days[0])      # Sun   first item
print(days[-1])     # Thu   last item
print(len(days))    # 5

print(days[1:3])    # ('Mon', 'Tue')
print(days[:2])     # ('Sun', 'Mon')
print(days[::-1])   # ('Thu', 'Wed', 'Tue', 'Mon', 'Sun')

print(days[10])     # IndexError!

fruits = ("apple", "banana")

fruits[0] = "kiwi"        # TypeError! can't change

temp = list(fruits)       # 1. make it a list
temp[0] = "kiwi"          # 2. change it
fruits = tuple(temp)      # 3. make it a tuple again
print(fruits)             # ('kiwi', 'banana')

print(fruits + ("mango",))   # ('kiwi', 'banana', 'mango')
print(("hi",) * 3)           # ('hi', 'hi', 'hi')
del fruits                   # delete the whole tuple

marks = (70, 90, 80, 90)

print(marks.count(90))    # 2   how many 90s
print(marks.index(80))    # 2   position of 80

print(len(marks))         # 4
print(max(marks))         # 90
print(min(marks))         # 70
print(sum(marks))         # 330
print(sorted(marks))      # [70, 80, 90, 90]  a list!
print(90 in marks)        # True
print((1, 2) == (2, 1))   # False

person = ("Ram", 20, "Pokhara")   # packing

name, age, city = person           # unpacking
print(name)      # Ram
print(age)       # 20

a, b = 1, 2
a, b = b, a      # swap values
print(a, b)      # 2 1

first, *rest = (1, 2, 3, 4)
print(rest)      # [2, 3, 4]

student = ("Ram", (2008, 5, 14), ["Math"])

print(student[1])        # (2008, 5, 14)
print(student[1][0])     # 2008

student[2].append("Art")    # OK! the list can change
print(student)
# ('Ram', (2008, 5, 14), ['Math', 'Art'])


t = (5, 10, 15, 20)

print(t[1])
print(t[-1])
print(t[1:3])
print(len(t))
print(t.index(15))

a, b, c, d = t
print(c)

t[0] = 1