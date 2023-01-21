list=[]
n=int(input("enter the size of the list"))
print("enter ",n," elements of the list")
for i in range(n):
    a=int(input())
    list.append(a)
print("sum is:",sum(list))

