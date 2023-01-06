class calculator:
    def addition(self):
        self.a=int(input("enter the value of a"))
        self.b=int(input("enter the value of b"))
        self.sum=self.a+self.b
        print("the additon value is:",self.sum)

    
    def difference(self):
        self.a=int(input("enter the value of a"))
        self.b=int(input("enter the value of b"))
        self.sub=self.a-self.b
        print("the diffrence value is:",self.sub)

    
    def product(self):
        self.a=int(input("enter the value of a"))
        self.b=int(input("enter the value of b"))
        self.mul=self.a*self.b
        print("the product value is:",self.mul)

    
    def reminder(self):
        self.a=int(input("enter the value of a"))
        self.b=int(input("enter the value of b"))
        self.div=self.a/self.b
        print("the division value is:",self.div)

cal=calculator()
print("1.ADD\n2.SUBRACTION\n3.MULTIPLY\n4.DIVISION\n")
choice=int(input("enter the choice:"))
if choice==1:
    cal.addition()
elif choice==2:
    cal.difference()
elif choice==3:
    cal.product()
elif choice==4:
    cal.reminder()
else:
    print("wrong choice")
