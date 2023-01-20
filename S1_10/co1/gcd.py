a=int(input("enter the first number"))
b=int(input("enter the second number:"))
while b!=0:
    r=a%b
    a=b
    b=r
print("the gcd of numbers are:",a)
