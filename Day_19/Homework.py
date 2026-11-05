from abc import ABC, abstractmethod

# 01 and 02
class Vehicle(ABC):
    @abstractmethod
    def wheels(self):
        pass

class Car(Vehicle):
    def wheels(self):
        return 4

class Bike(Vehicle):
    def wheels(self):
        return 2

# v = Vehicle()      

vehicles = [Car(), Bike()]
for v in vehicles:
    print(v.wheels())


# 03
class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def salary(self):
        pass

class Manager(Employee):
    def salary(self):
        return 90000

class Driver(Employee):
    def salary(self):
        return 25000

staff = [Manager("Ram"), Driver("Hari")]
for s in staff:
    print(s.name, s.salary())


# 04
class Mobile:
    def __init__(self):
        self.__battery = 100

    def get_battery(self):
        return self.__battery

    def use(self, amount):
        self.__battery = max(0, self.__battery - amount)

m = Mobile()
m.use(30)
print(m.get_battery())    # 70
m.use(500)
print(m.get_battery())    # 0, never below 0


# 05
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Not enough balance")
        else:
            self.__balance -= amount

acc = BankAccount(1000)
acc.withdraw(400)
print(acc.get_balance())    # 600
acc.withdraw(5000)          # Not enough balance


# 06
class User:
    def __init__(self, password):
        self.__password = password

    def login(self, password):
        if password == self.__password:
            print("Welcome")
        else:
            print("Wrong password")

u = User("abc123")
u.login("abc123")    # Welcome
u.login("wrong")     # Wrong password