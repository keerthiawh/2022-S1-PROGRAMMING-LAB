class rectangle:
    length=0
    breadth=0
    area=0
    def __init__(self):
        self.length=int(input("enter length of rectangle:"))
        self.breadth=int(input("enter breadth of rectangle:"))
    def Area(self):
        self.area=self.length*self.breadth
    def __lt__(self,other):
        if self.area<other.area:
            return True
        else:
            return False
    

print("first rectangle:")
obj1=rectangle()
print(" second rectangle:")
obj2=rectangle()
obj1.Area()
obj2.Area()
if obj1<obj2:
    print("area of  second rectangle is greatest")
else:
    print("area of first  rectangle is greatest")

