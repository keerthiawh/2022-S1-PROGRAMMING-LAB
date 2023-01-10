list_num = input("enter a list of integers:")
list_num = list_num.split()
list_num = [int(x) for x in list_num]
list_num = ['over' if x >100 else x for x in list_num]
print("all list",list_num)
