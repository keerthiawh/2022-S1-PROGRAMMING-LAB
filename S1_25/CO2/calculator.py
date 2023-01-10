def add(x,y):
    v=x+y
    print(a,"+",b,"=",v)
def sub(x,y):
    v=x-y
    print(a,"-",b,"=",v)
def mul(x,y):
    v=x*y
    print(a,"*",b,"=",v)
def div(x,y):
    v=x/y
    print(a,"+",b,"=",v)
print("select an option:")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.exit")
ch=int(input("enter the choice:"))
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
while(ch!=5):
    if(ch==1):
        v=add(a,b);
    elif(ch==1):
        v=sub(a,b);
    elif(ch==1):
        v=mul(a,b);
    elif(ch==1):
        v=add(a,b);
    else:
        print("invalid choice")
   
