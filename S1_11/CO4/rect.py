class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
l1=int(input("enter length of first rectangle:"))
b1=int(input("enter breadth of first rectangle:"))
r1=rectangle(l1,b1)
l2=int(input("enter length of second rectangle:"))
b2=int(input("enter breadth of second rectangle:"))
r2=rectangle(l2,b2)
print("area of first rectangle:",r1.area())
print("perimeter of first rectangle:",r1.perimeter())
print("area of second rectangle:",r2.area())
print("perimeter of second rectangle:",r2.perimeter())
if r1.area()>r2.area():
    print("area of first rectangle is greatest")
else:
    print("area of second rectangle is greatest")


