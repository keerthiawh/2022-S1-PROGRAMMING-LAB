class calculator():
    def read(self):
        self.a=int(input("enter the two numbers:"))
        self.b=int(input())
    def sum(self):
        print("sum=",self.a+self.b)
    def difference(self):
        print("difference=",self.a-self.b)
    def product(self):
        print("mul=",self.a*self.b)
    def division(self):
         print("div=",self.a/self.b)
obj1=calculator()
while True:
    obj1.read()
    print("1.addition 2.difference 3.multiplication 4.division")
    n=int(input("Select the option:"))
    if n==1:
        obj1.sum()
    elif n==2:
        obj1.difference()
    elif n==3:
        obj1.product()
    elif n==4:
        obj1.division()
    else:print("invalid")
    c=int(input("continue? 1.Yes,2.No"))
    if c==2:
        break
        

        
