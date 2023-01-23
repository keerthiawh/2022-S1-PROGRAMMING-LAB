#Sort dictionary in ascending and descending order
dic_num = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print("Original dictionary: ",dic_num)
print("Dictionary in ascending order: ",sorted(dic_num.items()))
print("Dictionary in descending order: ",sorted(dic_num.items(),reverse=True))