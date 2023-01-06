class Student:
    def display(self):
        self.name=input("enter your name")
        self.roll=input("enter your roll")
        self.course=input("enter your course")
        print("name=",self.name)
        print("roll=",self.roll)
        print("course=",self.course)
student=Student()
student.display()
