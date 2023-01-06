class calculator:
    def read(self):
        self.a=int(input("Enter the first number"))
        self.b=int(input("Enter the second number"))
    def add(self):
        print(self.a+self.b)
    def sub(self):
        print(self.a-self.b)
    def mul(self):
        print(self.a*self.b)
    def div(self):
        print(self.a/self.b)
obj1=calculator()
while True:
    
    
    obj1.read()
    print("1.add,2.sub,3.mul,4.div")
    choice=int(input("Enter you want"))
   


    if choice==1:
        obj1.add()
    elif choice==2:
        obj1.sub()
    elif choice==3:
        obj1.mul()
    elif choice==4:
        obj1.div()
    else:
        
        print("NO CHOICE")
    c=int(input("do you want to continue.1.yes,2.No:"))
    if c==2:
        break
        
        
    



