#Find the sum of all items in a list
size = int(input("Enter the size of the list : "))
list_num = []
for i in range(size):
    list_num.append(int(input("Enter the number : ")))
print("List is ",list_num)
print("The sum of all items in the list is : ",sum(list_num))