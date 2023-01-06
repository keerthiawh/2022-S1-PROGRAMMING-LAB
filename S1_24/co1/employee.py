class employee:
    def details(self,slry,grd,dept):
        self.salary=slry
        self.grade=grd
        self.departement=dept
        print(self.salary)
        print(self.grade)
        print(self.departement)
f1=employee()
x=int(input("enter the salary: "))
y=input("enter the grade : ")
z=input("enter the departement: ")
f1.details(x,y,z)
f2=employee()
x=int(input("enter the salary: "))
y=input("enter the grade: ")
z=input("enter the departemnt: ")
f2.details(x,y,z)
