class employee():
    def display(self):
        print("salary=",self.salary)
        print("grade=",self.grade)
        print("department=",self.department)
    def read(self):
        self.salary=input("enter your salary:")
        self.grade=input("enter your grade:")
        self.department=input("enter your department:")
obj1=employee()
obj1.read()
obj1.display()
obj2=employee()
obj2.read()
obj2.display()