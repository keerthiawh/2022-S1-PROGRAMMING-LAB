input_string = input('Enter elements of a list 1 separated by space: ')
print("\n")
lst1 = input_string.split()
# print list
print('list: ', lst1)

input_string = input('Enter elements of a list 2 separated by space: ')
print("\n")
lst2 = input_string.split()
# print list
print('list: ', lst2)

lst2 = ['3', '5', '2', '100', '12', '12']
sum1 = str(0)
sum2 = str(0)
if len(lst1) == len(lst2):
    print("both lists are of equal length")
else:
    print("Two lists have unequal length")
for x in lst1:
    sum1 = sum1 + x
for x in lst2:
    sum2 = sum2 + x
if sum1 == sum2:
    a = "equal"
else:
    a = "not equal"
print("Sum of two list are ", a)
for x in lst1:
    for y in lst2:
        if x == y:
            print(y, "Occurs in both list")
