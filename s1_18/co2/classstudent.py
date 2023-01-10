class Student:
    def read(self):
        self.roll_number=input("enter the roll_number:")
        self.name=input("enter ur name:")
        self.class_name=input("enter the class:")
    def display(self):
        print("roll number:",self.roll_number)
        print("name:",self.name)
        print("class:",self.class_name)

obj=Student()
obj.read()
obj.display()
