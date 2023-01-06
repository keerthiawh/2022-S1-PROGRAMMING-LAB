class employee:
    def display(self):
        print("\n salary:",self.salary)
        print("\n grade:",self.grade)
        print("\n department:",self.department)
    def read(self):     
        self.salary=int(input("enter salary:"))
        self.grade=input("enter grade:")
        self.department=input("enter department:")
        
obj1=employee()
obj2=employee()
obj3=employee()
obj1.read()
obj2.read()
obj3.read()
obj1.display()
obj2.display()
obj3.display()



        
