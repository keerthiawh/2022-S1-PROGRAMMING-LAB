class employee():
    def display(self):
        print("salary is:",self.salary)
        print("grade is:",self.grade)
        print("department is:",self.department)
    def read(self):
        self.salary=int(input("salary:"))
        self.grade=input("grade:")
        self.department=input("department:")
obj1=employee()
obj2=employee()
obj3=employee()
obj1.read()
obj2.read()
obj3.read()
obj1.display()
obj2.display()
obj3.display()
        
