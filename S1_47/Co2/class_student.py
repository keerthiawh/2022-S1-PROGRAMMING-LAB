class student:
    def display(self):
        print("roll  number",self.roll_no)
        print("name",self.name)
        print("class",self.class_name)
    def read(self):
        self.roll_no=int(input("enter roll number:"))
        self.name=input("enter name:")
        self.class_name=input("enter class:")
student=student()
student.read()
student.display()
