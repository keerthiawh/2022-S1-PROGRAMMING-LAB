txt=str(input("enter the text:"))
word=str(input("enter word"))
a=[]
count=0
a=str.split(" ")
for i in range(0,len(a)):
    if word==a[i]:
        count=count+1
print("count of word is:")
print(count)
