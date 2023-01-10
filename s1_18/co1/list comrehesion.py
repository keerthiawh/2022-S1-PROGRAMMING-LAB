list_num=[1,8,-9,-7,5,4]
print(list_num)
pos_num=[num for num in list_num if num>=0]
print("positive number in the list= ",*pos_num)
lst_1=[i*i for i in pos_num]
print("square of the positive number= ",*lst_1)
vowels=["a","e","i","o","u"]
name=input("enter the word")
new_str=[a for a in name if a in vowels]
print("vowels in that word are= ",*new_str)
orderd_lst=[ord(a) for a in name]
print("orderd value of each word in the list= ",*orderd_lst)
    
