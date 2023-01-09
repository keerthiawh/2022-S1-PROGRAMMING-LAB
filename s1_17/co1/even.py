list=[1,3,5,7,2,6,8]
print(list)
for i in list:
    if i%2==0:
       print(i)
       list.remove(i)
print(list)
