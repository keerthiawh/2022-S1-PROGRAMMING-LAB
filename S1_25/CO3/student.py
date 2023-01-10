class students():
    def disply(self):
        print("name:",self.name)
        print("rollno:",self.roll)
        print("course:",self.course)
    def read(self):
        self.name=input("enter the name:")
        self.roll=int(input("enter the rollno:"))
        self.course=input("enter the course:")
        print("\n")
obj1=students()
obj1.read()
obj1.disply()
