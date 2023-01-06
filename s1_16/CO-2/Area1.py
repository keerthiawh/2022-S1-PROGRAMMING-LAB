class triangle():
    def read(self):
        print("TRIANGLE")
        self.b=int(input("Enter the breadth"))
        self.h=int(input("Enter the height"))           
        self.l=int(input("Enter the length"))
    def area(self):
        print(1/2*self.b*self.h)
    def peri(self):
        print(self.b+self.h+self.l)
class rectangle():
    def read(self):
        print("RECTANGLE")
        self.b=int(input("Enter the breadth"))
                
        self.l=int(input("Enter the length"))
    def area(self):
        print(self.l*self.b)
    def peri(self):
        print(2*(self.b+self.l)) 
class square():
    
    def read(self):
        print("SQUARE")
        self.a=int(input("Enter the length"))
                
    def area(self):
        print(self.a*self.a)
    def peri(self):
        print(4*self.a)
obj1=triangle()
obj1.read()
obj1.area()
obj1.peri()
obj2=rectangle()
obj2.read()
obj2.area()
obj2.peri()              
obj3=square()
obj3.read()
obj3.area()
obj3.peri()
