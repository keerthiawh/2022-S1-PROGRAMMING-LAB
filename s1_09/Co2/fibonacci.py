def fibonacci(n):
    if n<=1:
     return n
    else:
       return(fibonacci(n-1)+fibonacci(n-2))
c=int(input("enter the limit:"))  
print("fibonacci series:")
for i in range(c):
 print(fibonacci(i))
     
