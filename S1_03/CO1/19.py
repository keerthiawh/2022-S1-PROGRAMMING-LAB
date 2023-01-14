a = int(input("Enter two numbers: "))
b = int(input())
while b != 0:
    r = a % b
    a = b
    b = r
print("gcd of given numbers is", a)
