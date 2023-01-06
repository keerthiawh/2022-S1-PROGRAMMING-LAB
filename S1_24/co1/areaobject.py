class areaperimeter:
    def area(self,a,b):
        self.length=a
        self.bredth=b
        self.area=a*b
        print(self.area)

f=areaperimeter()
x=int(input("enter the length : "))
y=int(input("enter the bredth : "))
f.area(x,y)
