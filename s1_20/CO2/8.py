def length(list1):
    list2=[]
    for i in list1:
        b=len(i)
        list2.append(b)
    
    
    a=max(list2)
    return a
list=[]

n=int(input("how many elements you are going to enter:"))
print("enter",n,"elements:")
for i in range(n):
    a=input()
    list.append(a)
print("list is",list)
v=length(list)
print("length of longest word is:",v)