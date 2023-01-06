list=[22,61,21,12,41]
print(list)
for i in list:
    if(i%2==0):
        list.remove(i)
print("list after removing even numbers")
print(list)
