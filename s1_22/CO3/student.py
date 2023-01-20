class student:
    def percentage(self,s1,s2,s3,s4,s5):
        p=((s1+s2+s3+s4+s5)/500)*100
        return p
    def display(self,name,rollNo,p):
        print("name:",name,"roll no",rollNo,"percentage",p)

obj=student()
