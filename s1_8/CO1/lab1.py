num=[1,-3,2,6,7,-55,33,99,45]
print(num)
newlst=[x for x in num if x>0]
print(newlst)
new_lst=[]
lst=[i*i for i in num]
print(lst)
vowel=['a','e','i','o','u']
name=input("enter the name:")
newstr=[x for x in name if x in vowel]
print(newstr)
ord_lst=[ord(x) for x in name]
print(ord_lst)
