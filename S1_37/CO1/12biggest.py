#Find biggest of 3 numbers entered.
num1 = int(input("Enter  the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1>num2 and num1>num3:
    print("The first number is the biggest ", num1)
elif num2>num1 and num2>num3:
    print("The second number is the biggest " , num2)
else:
    print("The third number is the biggest ", num3)
