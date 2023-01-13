n = int(input("Number of names: "))
lis = []
count = 0
for i in range(n):
    name = input("Enter the name: ")
    lis.append(name)
for i in lis:
    for j in i:
        if j == "a":
            count = count + 1
print("Count :", count)
