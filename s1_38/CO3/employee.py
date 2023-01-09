class employee:
    def display(self):
        print("details of employee",self.empnumber,":")
        print("salary:",self.salary)
        print("grade:",self.grade)
        print("department:",self.department)
        print("\n")
    def read(self):
        self.empnumber=int(input("enter the employee no.:"))
        self.salary=int(input("enter the salary:"))
        self.grade=input("enter the grade:")
        self.department=input("enter the department:")
        print("\n")
        
emp1=employee()
emp1.read()
emp2=employee()
emp2.read()
emp3=employee()
emp3.read()
emp1.display()
emp2.display()
emp3.display()
