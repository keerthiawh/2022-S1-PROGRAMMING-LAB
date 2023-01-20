class Calculator():
    def add(self):
        self.a=int(input("Enter a:"))
        self.b=int(input("Enter b:"))
        self.sum=self.a+self.b
        print("Sum is:",self.sum)
    def dif(self):
        self.a=int(input("Enter a:"))
        self.b=int(input("Enter b:"))
        self.min=self.a-self.b
        print("Difference is:",self.min)
    def mul(self):
        self.a=int(input("Enter a:"))
        self.b=int(input("Enter b:"))
        self.prod=self.a*self.b
        print("Product is:",self.prod)
    def div(self):
        self.a=int(input("Enter a:"))
        self.b=int(input("Enter b:"))
        self.rem=self.a/self.b
        print("Reminder is:",self.rem)
    def mod(self):
        self.a=int(input("Enter a:"))
        self.b=int(input("Enter b:"))
        self.md=self.a%self.b
        print("Modulus is:",self.md)
cal=Calculator()
print("1.Sum\n2.Difference\n3.Product\n4.Reminder\n5.Modulus")
ch=int(input("Enter your choice:"))
if ch==1:
    cal.add()
elif ch==2:
    cal.dif()
elif ch==3:
       cal.mul()
elif ch==4:
       cal.div()
elif ch==5:
       cal.mod()
else:
       print("Wrong Choice")
