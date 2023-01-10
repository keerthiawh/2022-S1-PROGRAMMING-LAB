class Calculator:
    def read(self):
        self.a=int(input("enter two numbers:"))
        self.b=int(input())
    def sum(self):
        print("sum is:",self.a+self.b)
    def diffrence(self):
        print("diffrence is:",self.a-self.b)
    def product(self):
        print("product is:",self.a*self.b)
    def division(self):
        print("division is:",self.a/self.b)

obj1=Calculator()
while True:
    obj1.read()
    print("1.addition 2.diffrence 3.product 4.division")
    n=int(input("enter the option you needed"))
    if n==1:
        obj1.sum()
    elif n==2:
        obj1.diffrence()
    elif n==3:
        obj1.product()
    elif n==4:
        obj1.division()
    else:print("invalid")
    c=int(input("do you want to continue.1.yes,2.no:"))
    if c==2:
        break
            
            
