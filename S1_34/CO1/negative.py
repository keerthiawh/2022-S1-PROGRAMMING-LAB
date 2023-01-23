n=[1,2,3,-5,6,-9,33,56,-10,-20]
print(n)
new=[x for x in n if x>0]
print(new)
lst1=[i*i for i in new]
print(lst1)
vowel=['a','e','i','o','u']
name=input()
new_str=[x for x in name if x in vowel]
print(new_str)
ord_lst=[ord(x) for x in name]
print(ord_lst)
