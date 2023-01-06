str1=input("enter a string: ")
word=input("enter the word you want to check:")
a=[]
count=0
a=str1.split(" ")
for i in range(0,len(a)):
    if(word==a[i]):
        count=count+1
print("the count of word is:")
print(count)
