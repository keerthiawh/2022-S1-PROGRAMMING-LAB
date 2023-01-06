def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

print("select an operation")
print("1.ADD")
print("2.SUBSTRATION")
print("3.MULTIPLICATION")
print("4.DIVISION")

while true:
    choice = input("enter choice(1-2-3-4): ")
    if choice in ("1","2","3","4"):
        num1 = float("enter the first number: ")
        num2 = float("enter the second number: ")

        if choice =='1':
            print(num1, "+",num2, "=",add(num1,num2))

        elif choice =='2':
            print(num1, "-",num2, "=",sub(num1,num2))

        elif choice =='3':
            print(num1,"*",num2, "=",mul(num1,num2))

        elif choice =='4':
            print(num1,"/",num2, "=",div(num1,num2))
    else:
        print("invalid input")
