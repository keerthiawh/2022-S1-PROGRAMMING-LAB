num=[1,-3,33,-44,99,33,-238,8383]
print(num)
new_lst=[x for x in num if x>0]
print(new_lst)
lst1=[i*i for i in new_lst]
print(lst1)
str1=input("enter a string")
print("the string is",str1)
vowel=['a','e','i','o','u']
res=[x for x in str1 if x in vowel]
print(res) 
ord_lst=[ord(x) for x in str1]
print(ord_lst)
