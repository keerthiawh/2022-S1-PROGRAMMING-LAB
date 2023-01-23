class calculator:
    a=int(input("enter a no:"))
    b=int(input("enter a no:"))
    def add(self):
        self.c=self.a+self.b
        print("sum:",self.c)
    def mul(self):
        self.c=self.a*self.b
        print("multiplication:",self.c)
    def diff(self):
        self.c=self.a-self.b
        print("difference:",self.c)
    def division(self):
        self.c=self.a/self.b
        print("division:",self.c)
    def mod(self):
        self.c=self.a%self.b
        print("mod value:",self.c)
c=calculator()
op=input("enter the operation +,*,-,/,%:")
if op=="+":
    c.add()
elif op=="*":
    c.multi()
elif op=="-":
    c.diff()
elif op=="/":
    c.div()
elif op=="%":
    c.mod()
else:
    print("invalid")