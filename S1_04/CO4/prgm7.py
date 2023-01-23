#Count the repeating words in a sentence : 
line="blue is a beautiful color the color blue is the color of sky"
print(line)
str=input("enter the word :")
a=line.split()

count=0
for i in a:
    if str==i:
        count=count+1
print(count)
