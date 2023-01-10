num=[11,-3,23,-5,9]
print(num)
new_list=[x for x in num if x>0]
print(new_list)
list_1=[i*i for i in new_list]
print(list_1)
vowel=['a','e','i','o','u']
name=input()
new_str=[x for x in name if x in vowel]
print(new_str)
ord_list=[ord(x) for x in name]
print(ord_list)
