class Student():
     
    
    def display(self):
        print(self.name)
        print(self.roll)
        print(self.course)
        


    def read(self):
        self.name=input("Enter the name:")
        self.roll=int(input("Enter the rollno:"))
        self.course=input("Enter the course:")

obj1=Student()
obj1.read()
obj1.display()

obj2=Student()
obj2.read()
obj2.display()

obj3=Student()
obj3.read()
obj3.display()
