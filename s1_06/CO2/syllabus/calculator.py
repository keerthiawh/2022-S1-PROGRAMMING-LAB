class calculator:
     a=int(input("enter first number:"))
     b=int(input("enter second number:"))

     def sum(self):
         c=self.a+self.b
         print("sum is:",c)
     def sub(self):
         c=self.a-self.b
         print("difference is:",c)
     def mul(self):
         c=self.a*self.b
         print("product is:",c)
     def div(self):
         c=self.a/self.b
         print("division is:",c)
     def mod(self):
         c=self.a%self.b
         print("mod is:",c)


while True:
    d1=calculator()
    d=input("enter operation:")
    if(d=='+'):
        d1.sum()
    elif(d=='-'):
        d1.sub()
    elif(d=='/'):
        d1.div()
    elif(d=='%'):
        d1.mod()
    d=int(input("do you want to continue 1.yes 2.no:"))
    if d==2:
        break
