list1 = []
n = int(input("Enter the size of the list: "))
print("Enter", n, "integers")
for i in range(n):
    a = int(input())
    list1.append(a)
print("List of integers:", list1)
list2 = [x for x in list1 if x % 2 != 0]
print("New list after removing even numbers:", list2)
