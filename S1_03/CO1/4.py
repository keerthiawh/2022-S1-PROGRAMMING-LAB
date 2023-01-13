str1 = input("Enter the string: ")
str2 = input("Enter the word: ")
a = str1.split()
count = 0
for i in a:
    if i == str2:
        count += 1
print(count)
