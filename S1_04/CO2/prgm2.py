num =int(input("Enter the number : "))
def fabi(n):
    a, b = 0, 1
    while a < n+1:
        print(a, end=' ')
        a, b = b, a+b
    print()

fabi(num)
