class Rectangle:
    __length=0
    __breadth=0
    __area=0
    def __init__(self):
        self.length=int(input("Enter the length:"))
        self.breadth=int(input("Enter the breadth:"))
    def Area(self):
        self.__area=self.__length*self.__breadth
    def __gt__(self,other):
        if self.__area>other.__area:
            return True
        else:
            return False
print("First rectangle:")
obj1=Rectangle()
print("Second triangle:")
obj2=Rectangle()
obj1.Area()
obj2.Area()
if(obj1>obj2):
    print("First")
else:
    print("Second")