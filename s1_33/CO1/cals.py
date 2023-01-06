def add(a,b):
    c=a+b
    print("sum is:",c)
def sub(a,b):
    c=a-b
    print("answer after sub is:",c)
def div(a,b):
    c=a/b
    print("answer after div is:",c)
def mul(a,b):
    c=a*b
    print("answer after mul",c)

x=int(input("enter the 1st number"))
y=int(input("enter the 2nd number"))
z=input("enter the operation")
if(z=='+'):
    add(x,y)
elif(z=='-'):
    sub(x,y)
elif(z=='/'):
    div(x,y)
elif(z=='*'):
    mul(x,y)
