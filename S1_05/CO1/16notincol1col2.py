#Print out all colors from color-list1 not contained in color-list2.

#Get color names from user
colors1 = input("Enter color names: ")
colors1 = colors1.split(",")
colors2 = input("Enter color names: ")
colors2 = colors2.split(",")
for color in colors1:
    if color not in colors2:
        print("This color not in the color2 ",color)
