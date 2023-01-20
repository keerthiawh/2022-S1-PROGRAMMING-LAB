class Employee:
    def display(self):
        print("salary",self.salary)
        print("grade",self.grade)
        print("department",self.department)
    def read(self):
        self.salary=int(input("Salary:"))
        self.grade=input("Grade:")
        self.department=input("department:")
emp1=Employee()
emp1.read()
emp1.display()
emp2=Employee()
emp2.read()
emp2.display()
emp3=Employee()
emp3.read()
emp3.display()

