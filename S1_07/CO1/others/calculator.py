#Calculator

def addition(x,y):
   return x+y

def subtraction(x,y):
   return x-y

def multiplication(x,y):
   return x*y

def division(x,y):
   return x/y

print("select operation")
print("1.addition")
print("2.subraction")
print("3.multiplication")
print("4.division")

while True:
    choice=input("enter choice:(1/2/3/4):")

    if choice in ('1','2','3','4'):
        num1=float(input("enter first number:"))
        num2=float(input("enter second number:"))

        if choice=='1':
            print(num1,"+",num2,"=",addition(num1,num2))

        elif choice=='2':
            print(num1,"-",num2,"=",subtraction(num1,num2))

        elif choice=='3':
            print(num1,"*",num2,"=",multiplication(num1,num2))
        elif choice=='4':
            print(num1,"/",num2,"=",division(num1,num2))
        else:
            print("invalid")

            
