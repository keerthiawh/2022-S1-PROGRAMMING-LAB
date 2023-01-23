#Generate a list of four digit numbers in a given range with all their digits even and thenumber is a perfect square.
list_num = []
for i in range(1000,9999):
    if i%2==0 and i%3==0 and i%5==0 and i%7==0:
        list_num.append(i)
print("List of four digit numbers in a given range with all their digits even and the number is a perfect square : ",list_num)

