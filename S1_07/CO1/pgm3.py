#(a)Positive numbers

num=[1,-3,2,33,-44,99,33,-238,8383]
print(num)
new_lst=[x for x in num if x>0]
print("postive numbers =",new_lst)
print()

#(b)Square of N Numbers

lst = []  
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele) 
print(lst)
lst1=[i*i for i in lst]
print("square of n Numbers =",lst1)

print()
print()

#(c)Form a list of vowels selected from a givenword

vowel=['a','e','i','o','u','A','E','I','O','U']
name = input("Enter Your name :")
new_str=[x for x in name if x in vowel]
print(new_str)

print()
print()

#(d)List Ordinal Values
ord_lst=[ord(x) for x in name]
print(ord_lst)

