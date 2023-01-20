class Student():
    def display(self):
        print("NAME:",self.name)
        print("ROLL NO:",self.roll)
        print("COURSE:",self.course)
    def read(self):
        self.name=input("Enter the name:")
        self.roll=int(input("Enter the roll number:"))
        self.course=input("Enter the course:")
obj1=Student()
obj1.read()
obj1.display()
obj2=Student()
obj2.read()
obj2.display()
