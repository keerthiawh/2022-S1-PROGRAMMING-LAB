num=[1,-3,2,33,-44,99,33,-238,8383]
print(num)
new_list=[x for x in num if x>0]
print (new_list)
list1=[i*i for i in new_list]
print(list1)
vowel=['a','e','i','o','u']
name=input("enter a name")
new_str=[x for x in name if x in vowel]
print(new_str)
ord_list=[ord(x) for x in name]
print(ord_list)
