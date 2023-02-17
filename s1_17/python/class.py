class student:
    def display(self,a,b):
        self.a=a
        self.b=b
        print("mcas1:")
        print(self.a)
        print("mcas2:")
        print("after merging")
        self.c=self.a+self.b
        print(self.c)
    def insert(self):
        (self.a).append("g")
        print(self.a)
    def sorting(self):
        print(sorted(self.a))
        print(sorted(self.b))
    def search(self,element):
        self.element=element
        if self.element in self.b:
            print("element found")
        else:
            print("not found")
mcas1=["a","c","b"]
mcas2=["f","e"]
obj1=student()
obj1.display(mcas1,mcas2)
print("enter inserting a new element to mcas1")
obj1.insert()
print("after sorting")
obj1.sorting()
n=input("enter the element to search:")
obj1.search(n)
