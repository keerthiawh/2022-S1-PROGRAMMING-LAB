class Rectangle:
    def display(self):
        print("Area:",self.area)
    def read(self):
        self.length=int(input("Enter the length:"))
        self.breadth=int(input("Enter the breadth:"))
    def calc(self,length,breadth):
        self.area=self.lenth*self.breadth
obj1=Rectangle()
obj1.calc()
obj1.read()
obj1.display()
