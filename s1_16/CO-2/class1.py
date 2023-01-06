class employee:
    def display(self,salary,grade,department):
        self.salary=salary
        self.grade=grade
        self.department=department
        print("salary:",self.salary)
        print("grade:",self.grade)
        print("department:",self.department)
employee1=employee()
employee1.display(5000,"A","IT")
employee2=employee()
employee2.display(7000,"A","IT")
employee3=employee()
employee3.display(9000,"B","marketing")





