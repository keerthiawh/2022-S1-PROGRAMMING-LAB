class rect:
    def area(self,length,breadth):
        self.l=length
        self.breadth=breadth
        self.area=length*breadth
        print("area = ",self.area)

obj=rect()
x=4
y=3
obj.area(x,y)
