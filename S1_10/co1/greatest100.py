list=[]
print("enter 5 element:")
for i in range(0,5):
    a=int(input())
    if a<100:
        list.append(a)
    else:
            list.append("over")
print(list)
