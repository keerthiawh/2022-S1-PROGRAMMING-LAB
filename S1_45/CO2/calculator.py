class Calc():
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    def add(self):
        self.c=self.a+self.b
        print("Sum is:",self.c)
    def sub(self):
        self.c=self.a-self.b
        print("Difference is:",self.c)
    def mul(self):
        self.c=self.a*self.b
        print("Product is:",self.c)
    def div(self):
        self.c=self.a/self.b
        print("Quotient is:",self.c)
    def mod(self):
        self.c=self.a%self.b
        print("Mode is:",self.c)
while True:
    
    c=Calc()
    op=input("Enter the operation +,-,*,/,%\n")
    if op=="+":
        c.add()
    elif op=="-":
        c.sub()
    elif op=="*":
        c.mul()
    elif op=="/":
        c.div()
    elif op=="%":
        c.mod()
    else:
        print("Invalid operator")
    c=int(input("Do you want to continue 1.yes,2.no"))
    if c==2:
        break
