class calc:
    a=int(input("enter a num:"))
    b=int(input("enter a num:"))
    def add(self):
        self.c=self.a+self.b
        print("sum is",self.c)
    def diff(self):
        self.c=self.a-self.b
        print("difference is",self.c)
    def mul(self):
        self.c=self.a*self.b
        print("multiplication value is",self.c)
    def div(self):
        self.c=self.a/self.b
        print("division value is",self.c)
    def mod(self):
        self.c=self.a%self.b
        print("mod value is",self.c)
c=calc()
op=input("enter the operation +,-,*,/,%::")
if op=="+":
    c.add()
elif op=="-":
    c.diff()
elif op=="*":
    c.mul()
elif op=="/":
    c.div()
elif op=="%":
    c.mod()
else :
    print("invalid")
