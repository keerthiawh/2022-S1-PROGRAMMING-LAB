dict1=[]
n1=int(input("total number of elements in dict 1 : "))
for i in range(n1):
    dict1[i]=input("enter element : ")
print(sorted(dict1.items(), key = lambda kv:(kv[1],kv[0])))
print(sorted(dict1.items(), key = lambda kv:(kv[1], kv[0]),reverse=True))
