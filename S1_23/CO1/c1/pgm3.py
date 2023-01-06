num=[1,-3,2,33,-44,99,33,-238,8383]
print(num)
new_lst=[x for x in num if x>0]
print(new_lst)
lst1=[i*i for i in new_lst]
print(lst1)
vowel=['a','e','i','o','u']
name=input()
new_str=[x for x in name if x in vowel]
print(new_str)
ord_lst=[ord(x) for x in name]
print(ord_lst)
