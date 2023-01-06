# Generate all factors of a number.
num = int(input("Enter the number : "))
def factors(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=" ")
    print()
factors(num)
