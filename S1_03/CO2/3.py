# Find the sum of all items in a list.
list = []
n = int(input("Enter the size of the list: "))
print("Enter ", n, "elements of the list")
for i in range(n):
    a = int(input())
    list.append(a)
print("sum is:", sum(list))