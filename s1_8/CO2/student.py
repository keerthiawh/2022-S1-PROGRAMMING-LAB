class Student():
    def display(self):
        print("NAME:",self.name)
        print("ROLL_NO:",self.roll)
        print("COURSE:",self.course)
    def read(self):
        self.name=input("enter the name:")
        self.roll=int(input("enter the roll number:"))
        self.course=input("enter the course:")
obj1=Student()
obj1.read()
obj1.display()
obj2=Student()
obj2.read()
obj2.display()
            
            
