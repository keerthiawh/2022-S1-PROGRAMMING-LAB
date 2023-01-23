class Rectangle():
    def display(self):
        print("Area=",self.area)
        print("Perimeter=",self.perimeter)

    def read(self):
        self.length=int(input("Enter the length"))
        self.breadth=int(input("Enter the breadth"))
        self.area=self.length*self.breadth
        self.perimeter=(self.length+self.breadth)/2




class Square():
    def display(self):
        print("Area=",self.area)
        print("Perimeter=",self.perimeter)

    def read(self):
        self.length=int(input("Enter the length"))
        self.area=self.length*self.length
        self.perimeter=4*self.length



class Triangle():
    def display(self):
        print("Area=",self.area)
        print("Perimeter=",self.perimeter)

    def read(self):
        self.s1=int(input("first side"))
        self.s2=int(input("second side"))
        self.s3=int(input("third side"))
        s=(self.s1+self.s2+self.s3)/2
        self.area=(s*(s-self.s1)*(s-self.s2)*(s-self.s3)) ** 0.5
        self.perimeter=self.s1+self.s2+self.s3
while True:
    
    x=int(input("1.Rectangle,2.Square,3.Triangle"))
    if x==1:
        a=Rectangle()
        a.read()
        a.display()
    elif x==2:
        b=Square()
        b.read()
        b.display()
    elif x==3:
        c=Triangle()
        c.read()
        c.display()
    else:
        print("Invalid input")
        break
