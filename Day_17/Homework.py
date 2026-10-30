class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def info(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")

b1 = Book("The lost Jungle", "J.K Author", 4000)
b2 = Book("Life comes from Life", "A.C Bhaktivedanta Srila Prabhupad", 4000)
b3 = Book("Science of Self Realization", "A.C Bhaktivedanta Srila Prabhupad", 5000)
print(f"Title: {b1.title}, Author: {b1.author}, Price: {b1.price}")
print(f"Title: {b2.title}, Author: {b2.author}, Price: {b2.price}")
print(f"Title: {b3.title}, Author: {b3.author}, Price: {b3.price}")
print("Using info method:")
b1.info()
b2.info()
b3.info()
