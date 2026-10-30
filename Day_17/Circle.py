class Circle:
    def __init__(self, radius):
        self.radius = radius

    def  area(self):
        return 3.14 * pow(self.radius, 2)
c1 = Circle(5)
print(c1.area())
class Counter():
    def __init__(self):
        self.count = 0

    def increase(self):
        self.count += 1

    def reset(self):
        self.count = 0

C1 = Counter()
C1.increase()
C1.increase()
C1.reset()

class Light():
    def __init__(self):
        self.is_on = False
    
    def switch(self):
        self.is_on = not self.is_on
        return self.is_on
l1 = Light()
print(l1.switch())
print(l1.switch())

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount
        return self.salary

e1 = Employee("Ram", 23000)
print(e1.give_raise(5000))