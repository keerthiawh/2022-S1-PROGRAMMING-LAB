class calculator():
    def add(self):
        self.a=int(input("enter the first no:"))
        self.b=int(input("enter the second no:"))
        self.sum=self.a+self.b
        print("the sum is:",self.sum)
    def sub(self):
        self.a=int(input("enter the first no:"))
        self.b=int(input("enter the second no:"))
        self.diff=self.a*self.b
        print("the difference is:",self.diff)
    def mul(self):
        self.a=int(input("enter the first no:"))
        self.b=int(input("enter the second no:"))
        self.mul=self.a*self.b
        print("the product is:",self.mul)
    def div(self):
        self.a=int(input("enter the first no:"))
        self.b=int(input("enter the second no:"))
        self.div=self.a*self.b
        print("the quoitent is:",self.div)
cal=calculator()
print("1.sum\n 2.difference\n3.multiplication\n4.division\n")
ch=int(input("enter your choice:"))
if ch==1:
    cal.add()
elif ch==2:
    cal.sub()
elif ch==3:
    cal.mul()
elif ch==4:
    cal.div()
else:
    print("invalid")
