p = int(input("enter the limit"))
for i in range(p):
    for j in range(i + 1):
        print('*', end="")
    print()
for i in range(p):
    for j in range(p - i - 1):
        print('*', end="")
    print()
