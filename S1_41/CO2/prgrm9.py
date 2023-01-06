def area(x):
    area(x)

length = []
breadth = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    element1 = int(input("enter the length"))
    element2 = int(input("enter the breadth"))
    length.append(element1)
    breadth.append(element2)

dict={}
value=[]
key=[]
for i in range(n):
    area=length[i]*breadth[i]
    value.append(area)
    key.append(i+1)
    dict[key[i]]=value[i]
print("dictionary is:\n",dict)
print("largest area is:",max(values))
