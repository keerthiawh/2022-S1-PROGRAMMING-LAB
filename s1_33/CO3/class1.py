class Student:
    def display(self):
        self.n = input("enter your name")
        self.rn = input("enter your roll.no")
        self.c = input("enter your course")
    print("n=",self.n)
    print("rn=",self.rn)
    print("c=",self.c)
s1=Student()
s1.display()

