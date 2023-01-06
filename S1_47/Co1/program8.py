str = input("Enter a string :")
l=len(str)
a=str[0]
str1=str.replace(a,"$")
str2=a+str1[1:l]
print(str2)
