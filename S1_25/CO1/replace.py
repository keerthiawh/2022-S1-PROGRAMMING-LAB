str1=input("enter a string ")
l=len(str1)
char=str1[0]
str1=str1.replace(char,'$')
str2=char+str1[1:l]
print(str2)


