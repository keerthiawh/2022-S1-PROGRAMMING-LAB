n=int(input("Enter the number of colors"))
list_color=[]
string=input("Enter the above number of colors separated by commas")
string1=string.split(',')
for i in range(0,n,1):
    list_color.append(string1[i])
print("The first color is:",list_color[0])
print("The last color is:",list_color[n-1])
