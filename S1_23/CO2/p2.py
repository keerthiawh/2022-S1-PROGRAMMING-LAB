class student:
    def display(self):
        self.rollnum=input("enter roll number: ")
        self.name=input("enter name: ")
        self.class_name=input("enter class: ")
        print("Roll number: ",self.rollnum)
        print("Name: ",self.name)
        print("Class: ",self.class_name)
Student= student()
Student.display()
