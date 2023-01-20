def fib(n):  
   a=0
   b=1
   count=0
   while(count<n):
      print(a)
      fib=a+b
      a=b
      b=fib
      count=count+1
n=int(input("Enter the number:"))
print("Fibonacci series:")
fib(n)
