class student:
    def display(self,rn,cls,nm):
        
       self.rollno=rn
       self.clas=cls
       self.name=nm
       print(self.rollno)
       print(self.clas)
       print(self.name)
f=student()
x=int(input("enter your rollno: "))
y=input("enter your class : ")
z=input("enter your name: ")
f.display(x,y,z)
          
    
