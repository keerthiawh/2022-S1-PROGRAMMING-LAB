def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print("select the operation")
print("1.add")
print("2.substract")
print("3.multiply")
print("4.divide")

while True:
    choice = input("enter choice :(1/2/3/4): ")

    if choice in('1','2','3','4'):
        num1 = float(input("enter first number: "))
        num2 = float(input("enter the second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1,num2))

    elif choice == '2':
        print(num1, "-", num2, "=", substract(num1,num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1,num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1,num2))

    else:print("invalid selection")

    next_calc = input("do you want to continue\n1.yes\n2.no: ")
    if next_calc == '2':
        break
        
