class number:
    def __init__(self):
        self.list1=[]
        self.list2=[]
        self.list3=[]
        n=int(input("enter the size of list1:"))
        for i in range(n):
            a=int(input())
            self.list1.append(a)
    def lists(self):
        self.list2=[x for x in self.list1 if x%2==0]
        self.list3=[x for x in self.list1 if x%3==0]
    def display(self):
        print("list you entered is :",self.list1)
        print("list of even numbers is:",self.list2)
        print("list of numbers divisible by 3:",self.list3)


obj1=number()
obj1.lists()
obj1.display()
