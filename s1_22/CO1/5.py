def factorial(a):
    factorial=1
    if a==0:
        print("factorial is 1")
    elif a<0:
        print("invalid")
    else:
        for i in range(1,a+1):
            factorial=factorial*i
        print("factorial is :",factorial)


x=int(input("enter the number"))
factorial(x)
            

        
