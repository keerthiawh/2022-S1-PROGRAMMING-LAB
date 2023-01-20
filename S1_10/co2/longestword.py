def lenlist(lst1):
    lst2=[]
    l=len(lst1)
    for i in lst1:
        a=len(i)
        lst2.append(a)
    f=max(lst1)
    return f
lst=input("enter the string seperated by comma:")
lstname=[]
lastname=lst.split(",")
v=lenlist(lstname)
print("the length of longest word in the lidt:",v)
    
