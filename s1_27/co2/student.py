class student :
    def display(self) :
        self.name=input("name")
        self.rollno=input("roll no")
        self.classname=input("clasname")

        print("name",self.name)
        print("rollno",self.rollno)
        print("classname",self.classname)
        
student=student()
student.display()                 
    
