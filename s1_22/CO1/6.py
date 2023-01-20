def sum_list(x):
    sum(x)
    
    
list=[]
n=int(input("enter the size of the list"))
print("enter the elements")
for i in range(0,n):
    a=int(input())
    list.append(a)
k=sum(list)
print("sum is: ",k)

