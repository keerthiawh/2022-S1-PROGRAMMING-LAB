def sum_list(x):
    sum(x)

lst=[]
n=int(input("enter the number of elements in list :"))
for i in range(0,n):
      element=int(input())
      lst.append(element)
print(lst)
             
print("sum of list = ",sum(lst))
