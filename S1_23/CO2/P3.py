class employee:
    def display(self,salary,grade,dept):
        self.salary=input("enter salary")
        self.grade=input("enter grade")
        self.dept=("enter dept")
        print("Salary: ",self.salary)
        print("Grade: ",self.grade)
        print("Department: ",self.dept)

print("employee 1")
emp1=employee()
emp1.display()
print("\n")
print("employee 2")
emp2=employee()
emp2.display()
print("\n")
print("employee 3")
emp3=employee()
emp3.display()