class A:
    def __init__(self):
        self.fruits=[]
        self.vegetables=[]
        print("enter 3 fruits")
        for i in range(3):
            a=input()
            self.fruits.append(a)
        print("enter 3 vegetables")
        for i in range(3):
            b=input()
            self.vegetables.append(b)
    def display(self):
        print("list of fruits:",self.fruits)
        print("list of vegetables:",self.vegetables)
    def vowels(self):
        
        self.dict={}
        vo=['a','e','i','o','u']
        for i in self.fruits:
            for a in i:
                if a in vo:
                    if a in self.dict:
                        self.dict[a]+=1
                    else:
                        self.dict[a]=1

        for i in self.vegetables:
            for a in i:
                if a in vo:
                    if a in self.dict:
                        self.dict[a]+=1
                    else:
                        self.dict[a]=1
        print(self.dict)
    def sort(self):
        print("sorted list of fruits is:",sorted(self.fruits))
        print("sorted list of vegetables is:",sorted(self.vegetables))
    def search(self):
        n=input("enter the fruit you want to search:")
        if n in self.fruits:
            print("present")
        else:
            print("not found")
        
                
        



obj1=A()
obj1.display()
obj1.vowels()
obj1.sort()
obj1.search()
