def ptrn1(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end=" ")
        print(" ")
def ptrn2(n):
    for i in range(n+1,0,-1):
        for j in range(0,i-1):
            print("*",end=' ')
        print(" ")
def ptrn3(n):
    k=(2*n)-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print("* ",end="")
        print("")
x=int(input("enter max height"))
ptrn1(x)
print("\n")
ptrn2(x)
ptrn3(x)
