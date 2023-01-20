class Employee:
    def display(self):
        print("Salary:",self.salary)
        print("Grade:",self.grade)
        print("Department:",self.department)
    def read(self):
        self.salary=int(input("Enter Your Salary:"))
        self.grade=input("Enter Your Grade:")
        self.department=input("Enter Your Department:")
obj1=Employee()
obj1.read()
obj1.display()
obj2=Employee()
obj2.read()
obj2.display()
obj3=Employee()
obj3.read()
obj3.display()
