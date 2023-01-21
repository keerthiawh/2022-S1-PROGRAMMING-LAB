class rectangle:
    def area(self,length,breadth):
        self.l=length
        self.b=breadth
        self.c=length*breadth
        print("area:",self.c)
    def Perimeter(self,length,breadth):
        c=2*(length+breadth)
        print("perimeter is:",c)
        
        
obj1=rectangle()
x=int(input("enter length and breadth"))
y=int(input())
obj1.area(x,y)
obj1.Perimeter(x,y)




