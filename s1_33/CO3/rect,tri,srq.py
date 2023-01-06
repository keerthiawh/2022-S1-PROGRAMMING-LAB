class rectangle:
    def findrect(self):
        self.l=int(input("enter the length of rectangle"))
        self.b=int(input("enter the breadth of rectangle"))
        self.area=self.l*self.b
        self.perimeter=2*(self.l+self.b)
        print("area of rectangle is:\n",self.area)
        print("perimeter of rectangle is:\n",self.perimeter)

class square:
    def findsqr(self):
        self.a=int(input("enter the side"))
        self.area=self.a*self.a
        self.perimeter=4*self.a
        print("area of square is:\n",self.area)
        print("perimeter of square is:\n",self.perimeter)

class triangle:
    def findtri(self):
        self.b=int(input("enter the breadth of triangle"))
        self.h=int(input("enter the height of triangle"))
        self.s=int(input("ente the side of triangle"))
        self.area=0.5*(self.b*self.h)
        self.perimeter=self.b+self.h+self.s
        print("area of triangle is:\n",self.area)
        print("perimeter of triangle is:\n",self.perimeter)


print("1.RECTANGLE\n2.SQUARE\n3.TRIANGLE\n")
choice=int(input("enter the choice:"))
if choice==1:
    r=rectangle()
    r.findrect()
elif choice==2:
    s=square()
    s.findsqr()
elif choice==3:
    t=triangle()
    t.findtri()

else:
    print("wrong choice")
