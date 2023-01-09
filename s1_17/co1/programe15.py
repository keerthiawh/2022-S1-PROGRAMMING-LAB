
list=[3,987,1067,-77,-7,4,-5,0]
print(list)
pos_num=[y for y in list if y>0]
print(pos_num)
num=[2,56,78,4,9,-77,-34,8765]
print(num)
new_num=[w for w in num if w>0]
print("positive number in the list= ",*new_num)
list1=[i*i for i in new_num]
print("sqaure of the positive number= ",*list1)
vowel=['a','e','i','o','u']
name=input("input the word")
new_str=[w for w in name if w in vowel]
print(new_str)
ord_list=[ord(w) for w in name]
print(ord_list)
