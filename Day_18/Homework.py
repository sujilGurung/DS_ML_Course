'''
Class Calculator with multiply(self, a, b, c=1). Test it with 2 and with 3 numbers
'''

class Calculator:

    def multiply(self, a, b, c=1):
        return a * b * c
        
c1 = Calculator()
print("Task 1")
print(c1.multiply(2, 3))
print(c1.multiply(2, 3, 2))

'''
Class Shop with total(self, *prices) that returns the sum of any number of prices'''
class Shop:
    def total(self, *prices):
        return sum(prices)
s1 = Shop()
print("Task 2")
print(s1.total(78, 66))
print(s1.total(5, 10, 15, 20))
print(s1.total())


'''Class Shape with area() that returns 0. Children Square and Circle override area()'''

class Shape:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        
    def area(self):
        return 0

class Square(Shape):
    def area(self):
        return pow(self.l, 2) 

class Cicle(Shape):
    def area(self):
        return 3.14 * pow(self.r, 2)
    
print("Task 3")
sq1 = Square(2, 3)
print(sq1.area())
c1 = Cicle(2, 3)
print(c1.area())

'''Class Person(name, age) and child Employee(name, age, salary) using super().__init__'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
e = Employee("Ram", 22, 23000)
print(e.name, e.age, e.salary)   

'''Multilevel: Vehicle → Car → ElectricCar, each adds one method. Call all three'''

class Vehicle:
    def start(self):
        print("Vehicle start")

class Car(Vehicle):
    def drive(self):
        print("Men drive Car")

class ElectricCar(Car):
    def charge(self):
        print("Car Recharging")

e = ElectricCar()
e.start()
e.drive()
e.charge()

'''Put a Square and a Circle in a list and print each area with a for loop'''
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

shapes = [Square(4), Circle(4)]

for s in shapes:
    print(s.area())