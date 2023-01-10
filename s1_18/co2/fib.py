def fibo(n):
    a=0
    b=1
    count=0
    if n<=0:
        print("invalid")
    elif n==1:
        print("fibanocci seies is: ",n)
    else:
        print("fibanocci series is: ")
        while count<n:
            print(a)
            c=a+b
            a=b
            b=c
            count=1
n=int(input("enter the limit"))
fibanocci(n)
            
