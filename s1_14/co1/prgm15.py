num=[2,-2,4,22,-16,108,22,-238,8383]
print(num)
new_lst=[x for x in num if x>0]
print(new_lst)
lst1=[i*i for i in new_lst]
print(lst1)
vowels=['a','e','i','o','u']
name=input("enter a name")
new_str=[x for x in name if x in vowels]
print(new_str)
