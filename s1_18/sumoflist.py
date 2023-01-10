def sum_list(x):
    sum(x)

list=[]
n=int(input("enter number of element in list : "))
for i in range(0,n):
    element=int(input())
    list.append(element)
print(list)
print("sum of list = ",sum(list))
