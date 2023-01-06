class rect:
    def area(self,length,breadth):
        self.length=length
        self.breadth=breadth
        self.area1=length*breadth
        print("area of rectangle:",self.area1)
    def perimeter(self,length,breadth):
        self.l=length
        self.b=breadth
        self.per1=2*(self.l+self.b)
        print("perimeter:",self.per1)
class square:
    def area(self):
        self.length=length
        self.area1=length*length
        print("area of square:",self.area1)
    def perimeter(self,length,breadth):
        self.l=length
        self.b=breadth
        self.per1=2*(self.l+self.b)
        print("perimeter:",self.per1)        
r1=rect()
x=int(input("enter the length:"))
y=int(input("enter the breadth:"))
r1.area(x,y)
r1.perimeter(x,y)
