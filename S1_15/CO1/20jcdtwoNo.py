#Find gcd of 2 numbers.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
if num1 > num2:
    num1,num2 = num2,num1
for i in range(1,num1+1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
print("GCD of two numbers is: ",gcd)
