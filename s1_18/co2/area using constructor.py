class Square:
    def _init_(self,a):
        self.sl=a
    def area(self):
        return self.sl**2
    def perimeter(self):
        return self.sl*4
class rectangle:
    def _init_(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
    def perimeter(self):
        return 2*(self.l+self.b)
class triangle:
    def _init_(self,b,h):
        self.sb=b
        self.sh=h
    def area(self):
        return 0.5*self.sb*self.sh
    def perimeter(self):
        return 0.5*self.sb*self.sh
    def perimeter(self):
        a=self.sb
        b=self.sh
        c=(a**2+b**2)**0.5
        return a+b+c
while True:
    print("menu:")
    print("1.Square:")
    print("2.rectangle:")
    print("3.triangle:")
    print("4.quit")
    choice=int(input("enter your choice: "))

    if choice==1:
        a=float(input("enter the length of square:"))
        Square=Square(a)
        print("area:" ,Square.area())
        print("perimeter:" ,Square.perimeter())
    elif choice==2:
        l=float(input("enter the length of rectangle: "))
        b=float(input("enter the breadth of rectangle: "))
        rectangle=rectangle(l,b)
        print("area:",rectangle.area())
        print("perimeter:",triangle.perimeter())
    elif choice==4:
        break
    else:
        print("invalid choice please try agian")
              
