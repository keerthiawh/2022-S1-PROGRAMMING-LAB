n=int(input("enter how many elements:"))
d={}
print("enter",n,"elements")
for i in range(1,n+1):
    d[i]=input()
print("dictionary is:",d)
d1=sorted(d.values())
d2=sorted(d.values(),reverse=True)
sorted_dict1={}
for i in  d1:
    for k in d.keys():
        if d[k]==i:
            sorted_dict1[k]=d[k]
print("dictionary in ascending order:")
print(sorted_dict1)
sorted_dict2={}
for i in  d2:
    for k in d.keys():
        if d[k]==i:
            sorted_dict2[k]=d[k]
print("dictionary in descending order is:",sorted_dict2)