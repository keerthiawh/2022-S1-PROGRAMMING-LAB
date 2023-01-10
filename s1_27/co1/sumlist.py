def sum_list(x):
    sum_list(x)

list=[]
n=int(input("enter the number of elements in list :"))
for i in range(0,n):
    element=int(input())
    list.append(element)
print(list)
print("sum of list = ",sum(list))
