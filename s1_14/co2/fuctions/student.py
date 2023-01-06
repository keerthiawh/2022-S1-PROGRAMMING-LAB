class student():


    def display(self):
        print(self.name)
        print(self.roll)
        print(self.course)


    def read(self):
        self.name=input("enter the name:")
        self.roll=int(input("enter the rollno:"))
        self.course=input("enter the course:")

obj1=student()
obj1.read()
obj1.display()

obj2=student()
obj2.read()
obj.display()

obj3=student()
obj3.read()
obj3.display()
