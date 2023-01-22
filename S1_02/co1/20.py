list1=[]
n=int(input("enter the size of the list:"))
print("enter",n,"integrs")
for i in range(n):
    a=int(input())
    list1.append(a)
print("list of integers:",list1)
list2=[x for x in list1 if x%2!=0]
print("new list after removing even numbers :",list2)