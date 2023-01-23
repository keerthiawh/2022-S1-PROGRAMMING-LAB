class Student():
     
    
    def display(self):
        print(self.name)
        print(self.roll)
        print(self.percentage)
        


    def read(self):
        self.name=input("Enter the name:")
        self.roll=int(input("Enter the rollno:"))
        self.mark1=int(input("Enter mark1:"))
        self.mark2=int(input("Enter mark2:"))
        self.mark3=int(input("Enter mark3:"))
        self.mark4=int(input("Enter mark4:"))
        self.mark5=int(input("Enter mark5:"))
        self.percentage=((self.mark1+self.mark2+self.mark3+self.mark4+self.mark5)/500)*100

obj1=Student()
obj1.read()
obj1.display()

