# Create a class Publisher (name). Derive class Book from Publisher with attributes title and author. Derive class Python from Book with attributes price and no_of_pages. Write a program that displays information about a Python book. Use base class constructor invocation and method overriding
class Publisher:
    def __init__(self, name):
        self.name = name
    def display(self):
        print("Publisher Name: ", self.name)
class Book(Publisher):
    def __init__(self, name, title, author):
        Publisher.__init__(self, name)
        self.title = title
        self.author = author
    def display(self):
        print("Book Title: ", self.title)
        print("Book Author: ", self.author)
class Python(Book):
    def __init__(self, name, title, author, price, no_of_pages):
        Book.__init__(self, name, title, author)
        self.price = price
        self.no_of_pages = no_of_pages
    def display(self):
        print("Book Price: ", self.price)
        print("Book Pages: ", self.no_of_pages)
python = Python("Calicut", "C++ Object Oriented Programming", "Arjun", 24.99, 350)
python.display()
b =Book("AWH", "Python 3 Object Oriented Programming", "Jaseem")
b.display()
p = Publisher("Calicut")
p.display()


