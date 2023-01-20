def pattern():
    rows=int(input("enter number of rows: "))
    for i in range(rows):
        for j in range(i+1):
            print("* ",end=" ")
        print("\n")
pattern()
def pattern2(rowss):
    for i in range(0,rowss):
        for j in range(0,i+1):
                print("* ",end=" ")
        print(" ")
        for i in range(rowss,0,-1):
            for j in range(0,i-1):
                print("* ",end=" ")
            print(" ")
rows2=int(input("enter the number of rows: "))
pattern2(rows2)
