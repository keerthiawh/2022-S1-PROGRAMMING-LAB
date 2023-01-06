def sum_list(r):
   sum(r)   
lst=[]
n=int(input("enter number of element in list:"))
for i in range(0,n):
    element=int(input())
    lst.append(element)
print(lst)
print("sum of list=",sum(lst))
