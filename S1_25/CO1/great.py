a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
if a>b and a>c:
    g=a;
elif b>c:
    g=b
else:
    g=c
print("the greatest no: ",g)
