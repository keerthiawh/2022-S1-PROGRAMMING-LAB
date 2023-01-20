r=int(input("enter the number"))
for i in range(r):
    for j in range(i + 1):
        print('*', end="")
    print()
for i in range(r):
    for j in range(r - i - 1):
        print('*', end="")
    print()
