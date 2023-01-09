list=[]
print("Enter 5 elements :")
for i in range(0,5):
    a=int(input())
    if a<100:
        list.append(a)
    else:
        list.append("Over")
print(list)
