class rectangle():
    def __init__(self):
        self.length=int(input("enter the length:"))
        self.breadth=int(input("enter the breadth"))
    def area(self):
        self.a=self.length*self.breadth
        print("area is:",self.a)
        return self.a
    def peri(self):
        self.p=2*(self.breadth+self.length)
        print("perimeter is:",self.p)
        return self.p
obj1=rectangle()
obj1.area()
obj1.peri()
obj2=rectangle()
obj2.area()
obj2.peri()
if(obj1.a>obj2.a):
    print("the area of first rectangle is graeter")
else:
    print("the area of second rectangle is greater")
