str1=input("enter 2 strings:")
str2=input()
l1=len(str1)
l2=len(str2)
a=str1[0]
b=str2[0]
str3=b+str1[1:l1]
str4=a+str2[1:l2]
str5=str3+" "+str4
print(str5)