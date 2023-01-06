class student():
    def display(self):
        print("Name:",self.name)
        print("Roll_no:",self.roll)
        print("Course:",self.course)
    def read(self):
        self.name=input("enter the name:")
        self.roll=int(input("enter the roll number:"))
        self.course=input("enter the course:")
obj1=student()
obj1.read()
obj1.display()
obj2=student()
obj2.read()
obj2.display()
