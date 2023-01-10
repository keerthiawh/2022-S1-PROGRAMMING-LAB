n=int(input("enter the number of colors"))
list_color=[]
string=input("enter the above number of colors seperated by comma")
string1=string.split(',')
for i in range(0,n,1):
    list_color.append(string1[i])
print("the first color is",list_color[0])
print("the last color is",list_color[n-1])
