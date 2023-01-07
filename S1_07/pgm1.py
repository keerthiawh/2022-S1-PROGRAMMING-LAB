class rectangle:
    def area(self,length,breadth):
        self.l=length
        self.b=breadth
        self.c=length*breadth
        print("area : ",self.c)
        return self.c
    def Perimeter(self,length,breadth):
        c=2*(length+breadth)
        print("Perimeter is :",c)
        
        
obj1=rectangle()
print("\nFirst Rectangle\n")
x=int(input("Enter Length :"))
y=int(input("Enter Breadth : "))
obj1.area(x,y)
obj1.Perimeter(x,y)

obj2=rectangle()
print("\nsecond Rectangle :\n")
x=int(input("Enter Length :"))
y=int(input("Enter Breadth : "))
obj2.area(x,y)
obj2.Perimeter(x,y)

if obj1.c < obj2.c:
    print("\n-------------------\nArea of Second Rectangle is Greater=",obj2.c)
elif obj1.c > obj2.c:
    print("\n-------------------\nArea of First Rectangle is Greater=",obj1.c)
else :
    print("\n-------------------\nArea Are Same\n")
