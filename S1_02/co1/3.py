list1=[22,-7,-9,1,4,5]
newlist=[x for x in list1 if x>0]
print(newlist)
n=int(input("enter"))
squarelist=[x*x for x in range(1,n+1)]
print(squarelist)
a=input("enter a string: ")
vowels=['a','e','i','o','u']
vowel_list=[x for x in a if x in vowels]
print(vowel_list)
ord_list=[ord(x) for x in a]
print(ord_list)
