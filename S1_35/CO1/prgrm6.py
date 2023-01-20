def sum_list(x):
    sum(x)
lst=[]
n=int(input("Enter number of element in list:"))
for i in range(0,n):
    element=int(input())
    lst.append(element)
print(lst)
print("Sum of list:",sum(lst))
