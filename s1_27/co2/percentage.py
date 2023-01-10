class Student :
    def display(self):
        print(self.name)
        print(self.rollno)
        print(self.percentage)

    def read(self):
        self.name=input("enter the name:")
        self.rollno=int(input("enter rollno:"))
        self.mark1=int(input("enter mark1:"))
        self.mark2=int(input("enter mark2:"))
        self.mark3=int(input("enter mark3:"))
        self.mark4=int(input("enter mark4:"))
        self.mark5=int(input("enter mark5:"))
        self.percentage=((self.mark1+self.mark2+self.mark3+self.mark4+self.mark5)/500)*100

obj1=Student()
obj1.read()
obj1.display()

obj2=Student()
obj2.read()
obj2.display()
