def factorial(a):
    fact=1
    if a==0:
        print("factorial is 1")
    elif a<0:
        print("invalid")
    else:
        for i in range(1,a+1):
            fact=fact*i
        print("factorial is:",fact)



x=int(input("enter a number:"))
factorial(x)