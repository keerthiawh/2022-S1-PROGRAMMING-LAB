lst=[]
n=int(input("enter the number of elements :"))
for i in range(0,n):
    a=int(input("enter the number"))
    if a<100:
        lst.append(a)
    else:
        lst.append("over")
print(lst)
