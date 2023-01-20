lst=[3,4,-33,543,-2234,324,-423]
print(lst)
lst_new=[x for x in lst if x>0]
print(lst_new)
lst_new2=[x*x for x in lst]
print(lst_new2)
vowels=['a','e','i','o','u']
string=input("Enter a word:")
lst_new3=[z for z in string if z in vowels]
print(lst_new3)
lst_new4=[ord(z) for z in string]
print(lst_new4)
