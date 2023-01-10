def pattern():
    rows=int(input("enter number of rows:"))
    for i in range(rows):
        for j in range(i+1):
            print("*",end=" ")
        print("\n")
pattern()
