class student:
    def display(self):
        self.roll_number=input("enter roll number:")
        self.name=input("enter name:")
        self.class_name=input("enter class:")
        print("\nroll number:",self.roll_number)
        print("name:",self.name)
        print("class:",self.class_name)
        
student = student()
student.display()
