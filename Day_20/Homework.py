'''01
Classes Dog, Cat and Duck, each with sound(). Put them in a list and call sound() in a for loop
02
Function play(instrument) that calls instrument.play_music(). Make Guitar, Madal and Flute
03
Parent Shape with area(). Children Square, Rectangle, Circle. Print the total area of a list of shapes
04
Parent Animal with sound(). Children Dog and Cat override it, Fish does not. Guess the output, then run it
05
Abstract class Notification with abstract send(msg). Children SMS, Email and Viber
06
Class Calculator with multiply() that works with 2 or 3 numbers (use a default value)'''

from abc import ABC, abstractmethod

class Dog():
    def sound(self):
        return "Woof"

class Cat():
    def sound(self):
        return "Meow"

class Duck():
    def sound(self):
        return "Quack"

print("Question 1")
sounds = [Dog(), Cat(), Duck()]
for s in sounds:
    print(s.sound())    



class Guitar:
    def play_music(self):
        return "Playing guitar"

class Madal:
    def play_music(self):
        return "Playing madal"

class Flute:
    def play_music(self):
        return "Playing flute"

def play(instrument):
    return instrument.play_music()

print("\nQuestion 2")
print(play(Guitar()))
print(play(Madal()))
print(play(Flute()))   

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
print("\nQuestion 3")
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

shapes = [Square(4), Rectangle(3, 5), Circle(2)]
total_area = sum(shape.area() for shape in shapes)
print("Total area:", total_area)

class Animal():
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

class Fish(Animal):
    pass

print("\nQuestion 4")
animals = [Dog(), Cat(), Fish()]
for animal in animals:
    print(animal.sound())

class Notification(ABC):
    @abstractmethod
    def send(self, msg):
        pass

class SMS(Notification):
    def send(self, msg):
        return f"Sending SMS: {msg}"

class Email(Notification):
    def send(self, msg):
        return f"Sending Email: {msg}"

class Viber(Notification):
    def send(self, msg):
        return f"Sending Viber: {msg}"

print("\nQuestion 5")
messages = ["Hello", "How are you?", "Goodbye"]
for msg in messages:
    print(SMS().send(msg))
    print(Email().send(msg))
    print(Viber().send(msg))

print("\nQuestion 6")
class Calculator:
    def multiply(self, a, b, c=2):
        return a * b * c

calc = Calculator()
print(calc.multiply(2, 4))
print(calc.multiply(2, 4, 3))