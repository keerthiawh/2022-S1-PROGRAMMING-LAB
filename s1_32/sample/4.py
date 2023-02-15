class checker:
    def __init__(self):
        self.list1=[]
        self.list2=[]
        self.n=int(input("enter how many elements:"))
        print("enter ",self.n,"elements")
        for i in range(self.n):
            a=int(input())
            self.list1.append(a)
        self.m=int(input("enter the size of second list:"))
        print("enter elements of second list")
        for i in range(self.m):
            b=int(input())
            self.list2.append(b)
    def display(self):
        print("first list is",self.list1)
        print("second list is",self.list2)
    def length(self):
        if self.m==self.n:
            print("equal length")
        else:
            print("not equal length")
    def sum(self):
        if sum(self.list1)==sum(self.list2):
            print("sums are equal")
        else:
            print("not equal")
    def occurance(self):
        flag=0
        for i in self.list1:
            if i in self.list2:
                flag=1
                break

            
            
        if flag>0:
            print("elements occur in both lists")
        else:
            print("no elements occur in both lists")
        
             
        
        
obj1=checker()
obj1.display()
obj1.length()
obj1.sum()
obj1.occurance()
            
