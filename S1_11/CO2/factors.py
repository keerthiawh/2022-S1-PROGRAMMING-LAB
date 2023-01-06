def fact(n):
    i=1
    while i<=n:
        if n%i==0:
            print(i)
        i=i+1
num=int(input("enter the number:"))
print("the factors of ",num,":")
fact(num)
