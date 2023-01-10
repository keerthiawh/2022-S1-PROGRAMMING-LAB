class employee():
    def display(self):
        print(self.name)
        print(self.salary)
        print(self.grade)
        print(self.departement)

    def read(self):
        self.name=input("enter the name:")
        self.salary=int(input("enter salary:"))
        self.grade=input("enter grade:")
        self.departement=input("enter departement:")

obj1=employee()
obj1.read()
obj1.display()

obj2=employee()
obj2.read()
obj2.display()

obj3=employee()
obj3.read()
obj3.display()


