class Employee():


    def display(self):
        print(self.sal)
        print(self.grade)
        print(self.dept)


    def read(self):
        self.sal=input("enter the salary:")
        self.grade=input("enter the grade:")
        self.dept=input("enter the department:")

obj1=Employee()
obj1.read()
obj1.display()

obj2=Employee()
obj2.read()
obj.display()

obj3=Employee()
obj3.read()
obj3.display()
