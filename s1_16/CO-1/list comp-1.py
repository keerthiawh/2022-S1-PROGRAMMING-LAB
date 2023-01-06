list_integers=[-1,-2,-3,4,5,6,7,8,9]
print(list_integers)
list_positive=[x for x in list_integers if x>=0]
print(list_positive)
integers=[i*i for i in list_positive]
print(integers)
vowel=['a','e','i','o','u']
name=input("enter the string")
str=[x for x in name if x in vowel]
print(str)
ord_list=[ord(x) for x in name]
print(ord_list)

