class Rectangle():
    arc=0
    p=0
    def __init__(self,breadth,length):
       self.breadth=breadth
       self.length=length
    def area(self):
        return self.breadth*self.length
    def perimeter(self):
        return 2*(self.breadth+self.length)
    def read(self):
        self.length=float(input("enter the length:"))
        self.breadth=float(input("enter the breadth:"))
r=Rectangle()
r2=Rectangle()
r.read()
r.perimeter()
r.area()

r2.read()
r2.perimeter()
r2.area()
if r.area>r2.area:
    print("r1 is the greater")
else:
    print("r2 is the greater")