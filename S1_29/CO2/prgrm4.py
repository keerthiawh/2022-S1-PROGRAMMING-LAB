def fibo(m):
    n1=0
    n2=1
    count=0
    if m<=0:
        print("invalid")
    elif m==1:
        print("Fibonacci series is:")
        print(n1)
    else:
        print("Fibonacci series is:")
        while count<m:
            print(n1)
            n=n1+n2
            n1=n2
            n2=n
            count+=1


a=int(input("enter the limit: "))
fibo(a)
