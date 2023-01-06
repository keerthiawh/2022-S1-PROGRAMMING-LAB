class employee():
    def display(self):
        print(self.salary)
        print(self.grade)
        print(self.department)
    def read(self):
        self.salary=input("Enter the salary")
        self.grade=input("Enter the grade")
        self.department=input("Enter the department")
obj1=employee()
obj2=employee()
obj3=employee()

obj1.read()
obj2.read()
obj3.read()
obj1.display()
obj2.display()
obj3.display()
