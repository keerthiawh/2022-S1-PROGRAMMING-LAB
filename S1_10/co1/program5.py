a=input("enter a string:")
b=a[10]
s=a[1:len(a)]
for i in range(len(s)):
if s[i]==a[10]:
b=b+"$"
else:
b=b+s[i]
