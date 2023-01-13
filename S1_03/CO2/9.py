# Create following pattern using nested loop
#
##
###
####
#####
####
###
##
#
n = int(input('Enter the number of rows: '))
for i in range(0, n):
    for j in range(0, i + 1):
        print("* ", end=" ")
    print(" ")

for i in range(n, 0, -1):
    for j in range(0, i - 1):
        print("* ", end=" ")
    print(" ")
