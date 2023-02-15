#Square of N numbers
num = int(input("Enter a number: "))
list_num = [x for x in range(1, num+1, 1)]
print("All list ", list_num)
list_sq = [x*x for x in list_num]
print("Square list ", list_sq)
