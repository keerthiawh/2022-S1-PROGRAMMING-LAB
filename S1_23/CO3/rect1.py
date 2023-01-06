class rectangle:
    width1=0
    length1=0
    area1=0
    peri1=0
    def __init__(self,length,width):
        self.length1=length
        self.width1=width
    def calc_area(self):
        self.area1=self.length1*self.width1
        print("area is:",self.area1)
    def calc_perimeter(self):
        self.peri1=2*(self.length1+self.width1)
        print("perimeter is:",self.peri1)
    def comp(self):
        if self.area1==self.peri1:
            print("both are equal")
        elif self.area1<=self.peri1:
            print("area is lesser than perimeter")
        elif self.area1>=self.peri1:
            print("area is greater than perimeter")
        else:
            print("invalid")
while(True):
    leng=int(input("enter the length of the rectangle:"))
    wid=int(input("enter the width of the rectangle:"))
    obj=rectangle(leng,wid)
    opt=input("a.area\nb.perimeter\noption:")
    if opt=='a':
        obj.calc_area()
    elif opt=='b':
        obj.calc_perimeter()
    else:
        print("options are wrong!")
obj.comp()












        
