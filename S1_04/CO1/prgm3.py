integer[-3,8,4,7,-9,70,-54,35,66,-8,-88]
print(integers)
new=[x for x in integers if x>0]
print("list of positive numbers:",new]
square=[]
n=int(input("Enter limit:"))
for i in range(1,n):
    square.append(i*i)
print("square:",square)
vowel=['a','e','i','o','u']
str=input("Enter string:")
str_vowel=[x for x in str if x in vowel]
print("vowel:",str_vowel)
ord_list=[ord (x) for x in str]
print("ordinal number:",ord_list)
