str1=input("enter a string")
l=len(str1)
f=str1[0]
e=str1[-1]
str2=str1.replace(f,e)
str2=str1.replace(e,f)
print(str2)
