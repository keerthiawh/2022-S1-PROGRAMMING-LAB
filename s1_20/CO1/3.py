list1=[22,7,-9,1,-4,5]
newlist=[x for x in list1 if x<0]
print(newlist)
squarelist=[x*x for x in list1]
print(squarelist)
vowels=["a","e","i","o","u"]
str=input("enter  a string")
vowel_list=[x for x in str if x in vowels]
print(vowel_list)
ord_list=[ord(x) for x in str]
print(ord_list)
