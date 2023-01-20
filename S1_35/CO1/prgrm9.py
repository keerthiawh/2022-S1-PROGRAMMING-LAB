list1=[]
list2=[]
n=int(input("Enter how many elements:\n"))
print("Enter",n,"lengths")
for i in range(n):
    a=int(input())
    list1.append(a)
print("Enter",n,"breadths")
for i in range(n):
    a=int(input())
    list2.append(a)

dict={}
value=[]
keys=[]
for i in range(n):
    area=list1[i] * list2[i]
    value.append(area)
    keys.append(i+1)
    dict[keys[i]]=value[i]
print("Dictionary is:\n",dict)
print("Maximum area is:\n",max(value))
