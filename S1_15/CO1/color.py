#Create a list of colors from comma-separated color names entered by user. Display first and last colors.

#Get color names from user
colors = []
for i in range(0,5,1):
    color = input("Enter color name: ")
    colors.append(color)
#Display first and last colorsr
print("First color: ", colors[0])
print("Last color: ", colors[-1])

