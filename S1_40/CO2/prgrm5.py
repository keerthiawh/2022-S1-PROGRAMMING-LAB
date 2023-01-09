def fact():
    f=1
    i=1
    while i<=5:
        f=f*i
        i=i+1
    print("factorial of number is:",f)

a=int(input("enter the limit:"))
fact()
