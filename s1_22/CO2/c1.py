class Employee:
    def display(self):
        print("salary:",self.salary)
        print("grade:",self.grade)
        print("department:",self.department)
    def Read(self):
        self.salary=int(input("enter salary:"))
        self.grade=input("enter grade:")
        self.department=input("enter department:")

obj1=Employee()
obj2=Employee()
obj3=Employee()
obj1.Read()
obj2.Read()
obj3.Read()
obj1.display()
obj2.display()
obj3.display()
