list1=[]
list2=[]
n1=int(input("enter size of first list"))
n2=int(input("enter size of second list"))
print("enter",n1,"colors of the first list")
for i in range(n1):
    a=input()
    list1.append(a)
                   
print("enter",n2,"colors of the first list")
for i in range(n2):
    b=input()
    list2.append(b)
print("first list is",list1)
print("second list is",list2)
list3=[x for x in list1 if x not in list2]
print("colors not in list 2",list3)