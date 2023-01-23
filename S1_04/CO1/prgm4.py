str=input("Enter a string:")
a=input("Enter the word you want to check:")
str1=str.split()
count=0
for i in str1:
    if i == a:
        count = count+1
print("Number of occurenece of the entered word:",count)    
