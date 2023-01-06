def sum_list(x):
    sum(x)
    
list=[]
n=int(input("enter noumber of elements in list :"))
for i in range(0,n):
    element=int(input())
    list.append(element)
print(list)    
print("sum of list = ",sum(list))
