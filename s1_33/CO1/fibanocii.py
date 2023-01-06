def fibonacci(n):
  fib_list = [1, 1]
  for i in range(n - 2):
    fib_list.append(fib_list[-1] + fib_list[-2])
  return fib_list
n = int(input("Enter the number of Fibonacci numbers to generate: "))
print(fibonacci(n))
