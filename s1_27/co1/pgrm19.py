vowel=['a','e','i','o','u']
print("enter a string")
name=input()
new_str=[x for x in name if x in vowel]
print(new_str)
ord_list=[ord(x) for x in name]
print(ord_list)
