class rectangle:
    def __init__(self):
        self.a=int(input("enter length and breadth of the rectangle:"))
        self.b=int(input())
        print("area is:",self.a*self.b)
        print("perimeter is:",2*(self.a+self.b))
class square:
    def __init__(self):
        self.a=int(input("enter the side of the square:"))
        print("area is :",self.a*self.a)
        print("perimeter is:",4*self.a)
class triangle:
    def __init__(self):
        self.b=int(input("enter base and height of the triangle:"))
        self.h=int(input())
        area=0.5*self.b*self.h
        perimeter=(self.b**2+self.h**2)**0.5
        print("area is:",area)
        print("perimeter is :",perimeter)

while True:
    r=int(input("find area and perimeter of:\n 1.rectangle\n 2.square\n 3.triangle\n"))
    if r==1:
        obj1=rectangle()
    elif r==2:
        obj1=square()
    elif r==3:
        obj1=triangle()
    else:print("invalid")
    c=int(input("do you want to continue:\n 1.yes\n 2.no"))
    if c==2:
        break

      

    



    
        
        
    

                   
        
