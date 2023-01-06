list_num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
list_not_even = []
print("Original list: ",list_num)
for i in list_num:
    if i % 2 != 0:
        list_not_even.append(i)
print("List of odd numbers: ",list_not_even)