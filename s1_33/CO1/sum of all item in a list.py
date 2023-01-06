def sum():
 lst = []
 num = int(input("how many numbers "))

 for n in range (num):
    numbers = int(input("enter the numbers:"))
    lst.append(numbers)

 s = 0
 for i in lst:
    s = s+i
    i = i+1


 print("sum of elements in given list is:", s)

sum()
