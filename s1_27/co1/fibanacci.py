def fib(n):
    n1=0
    n2=1
    count=0
    if n<=0:
        print("invalid")
    elif n==1:
        print("0")
    else :
        print("the fibanacci series is;")
        while count<n:
            print(n1)
            temp=n1+n2
            n1=n2
            n2=temp
            count+=1

a=int(input("enter the limit:"))
fib(a)
