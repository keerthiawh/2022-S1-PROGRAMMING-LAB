class Rectangle:
    __length=0
    __breadth=0
    __area=0
    def __init__(self):
        self.__length=int(input("Enter the length:"))
        self.__breadth=int(input("Enter the breadth:"))
    def Area(self):
        self.__area=self.__length*self.__breadth
    def __lt__(self,other):
        if self.__area<other.__area:
            return True
        else:
            return False

print("first rectangle:")
obj1=Rectangle()
print("second rectangle:")
obj2=Rectangle()
obj1.Area()
obj2.Area()
if obj1<obj2:
    print("Area of second rectangle is greater")
else:
    print("Area of first rectangle is greater")