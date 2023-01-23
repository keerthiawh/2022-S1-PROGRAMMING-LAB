def sum_list(x):
    sum(x)


lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
	element = int(input())
	lst.append(element) 
	
print(lst)
print("sum of list=",sum(lst))

