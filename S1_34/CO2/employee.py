class Employee():
     
    
    def display(self):
        print(self.sal)
        print(self.grade)
        print(self.dept)
        


    def read(self):
        self.sal=input("Enter the salary")
        self.grade=input("Enter the grade")
        self.dept=input("Enter the department")

obj1=Employee()
obj1.read()
obj1.display()

obj2=Employee()
obj2.read()
obj2.display()

obj3=Employee()
obj3.read()
obj3.display()
