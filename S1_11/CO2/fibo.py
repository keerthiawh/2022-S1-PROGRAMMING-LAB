def fibonacci(n):
    a=0
    b=1
    c=1
    while(c<n):
        print(c)
        c=a+b
        a=b
        b=c
n=int(input("enter a limit:"))
print("fibonacci series upto ",n)
fibonacci(n)
   
    
