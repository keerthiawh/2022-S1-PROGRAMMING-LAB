def PerfectSquare(n):
    return round(n**0.5)**2==n

Range=int(input("enter a range "))
list1=[]
for i in range(1000,9999):
    list1.append(i)
list2=[x for x in list1 if PerfectSquare(x)]
list3=[]
for i in list2:
    for j in i:
        print
        if j%2==0:
            list3.append(i)
print(list3)




       
       
