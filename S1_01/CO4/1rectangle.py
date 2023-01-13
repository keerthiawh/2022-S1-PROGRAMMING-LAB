# Create Rectangle class with attributes length and breadth and methods to find area and perimeter. Compare two Rectangle objects by their area.

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

l = int(input("Enter object r1 length: "))
b = int(input("Enter object r1 breadth: "))
r1 = Rectangle(l, b)
l = int(input("Enter object r2 length: "))
b = int(input("Enter object r2 breadth: "))
r2 = Rectangle(l, b)
print("Area ")
print("Area of r1:", r1.area())
print("Perimeter of r1:", r1.perimeter())

print("Area of r2:", r2.area())
print("Perimeter of r2:", r2.perimeter())

if r1.area() > r2.area():
    print("Area of r1 is greater than r2" , r1.area())
else:
    print("Area of r2 is greater than r1", r2.area())


