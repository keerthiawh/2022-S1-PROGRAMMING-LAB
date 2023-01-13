# Display the given pyramid with step number accepted from user.
def pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j * i, end=" ")
        print("\n")


n = int(input("Enter the limit: "))
pattern(n)
