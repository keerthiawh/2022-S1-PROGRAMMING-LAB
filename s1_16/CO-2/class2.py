class employee:
    def display(self,salary,grade,department):
        self.salary=salary
        self.grade=grade
        self.department=department
        print("salary:",self.salary)
        print("grade:",self.grade)
        print("department:",self.department)
    employee1=employee()
    salary=int(input("Enter the salary:"))
    grade=input("Enter the grade")
    department=input("Enter the department:")           
    display(employee1)
