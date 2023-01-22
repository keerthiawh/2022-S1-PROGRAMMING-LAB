def sum_list(a):
    return a
list=[]

n=int(input("how many numbers you are going to enter:"))
print("enter",n,"elements:")
for i in range(n):
    b=int(input())
    list.append(b)
    s=sum_list(b)
print(list)
print(s)