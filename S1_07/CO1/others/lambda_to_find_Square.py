list1=[]
a=int(input("enter the size of the list"))
print("enter ",a," elements of the list")
for i in range(a):
    b=int(input())
    list1.append(b)
print(list1)
list2=list(filter(lambda x:(x%2!=0),list1))
print(list2)
list3=list(filter(lambda x:(x%2==0),list1))
print(list3)

a=int(input("enter a number to find square:"))
square=lambda x:(x*x)
print("result is",square(a))
