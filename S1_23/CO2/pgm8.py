def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

print("Select operation")
print("1.ADD")
print("2.SUBSTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")

while True:
    choice=input("enter choice(1/2/3/4): ")
    if choice in ('1','2','3','4'):
        num1=int(input("enter first number: "))
        num2=int(input("enter second number: "))

        if choice =='1':
            print(num1,"+",num2, "=",add(num1,num2))

        elif choice =='2':
            print(num1,"-",num2, "=",sub(num1,num2))

        elif choice =='3':
            print(num1,"*",num2, "=",mul(num1,num2))

        elif choice=='4':
            print(num1,"/",num2, "=",div(num1,num2))

        new_calculation=input("do new calculation?? (y/n):")
        if new_calculation=="n":
            break
    else:
        print("invalid input")
