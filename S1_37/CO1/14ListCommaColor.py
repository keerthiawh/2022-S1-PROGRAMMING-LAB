#Create a list of colors from comma-separated color names entered by user. Display first and last colors.

#Get color names from user
colors = input("Enter color names: ")
colors = colors.split(",")
#Display first and last colors
print("First color: ", colors[0])
print("Last color: ", colors[-1])
