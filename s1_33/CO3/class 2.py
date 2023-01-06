class employee:
    def emp(self):
        self.department=input("enter the department:")
        self.grade=input("enter the grade:")
        self.salary=int(input("enter your salary:"))
    def display(self):
        print("department=",self.department)
        print("grade=",self.grade)
        print("salary=",self.salary)

print("details of employees:")
e1=employee()
e2=employee()
e3=employee()
e1.emp()
e2.emp()
e3.emp()
e1.display()
e2.display()
e3.display()
