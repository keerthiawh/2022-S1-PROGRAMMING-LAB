class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
    def peri(self):
        return 2*(self.breadth+self.length)
a=int(input("Enter length of first rectangle: "))
b=int(input("Enter breadth of first rectangle: "))
c=int(input("Enter length of second rectangle: "))
d=int(input("Enter breadth of second rectangle: "))
obj=rectangle(a,b)
obj1=rectangle(c,d)
print("Area of first rectangle: ",obj.area())
print("Perimeter of first rectangle: ",obj1.peri())
print("Area of second rectangle: ",obj1.area())
