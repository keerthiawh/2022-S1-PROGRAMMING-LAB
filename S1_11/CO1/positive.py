num=[2,6,-4,7,-1,-5]
print(num)
new_list=[x for x in num if x>0]
print("positive integers from the list")
print(new_list)
lst=[]
n=int(input("enter the no of elements"))
for i in range(0,n):
    a=int(input("enter a number:"))
    lst.append(a)
list1=[i*i for i in lst]
print(list1)
str1=input("enter a string: ")
print("the string is: ",str1)
vowel=['a','e','i','o','u']
res=[x for x in str1 if x in vowel]
print(res)
ord_lst=[ord(x) for x in str1]
print(ord_lst)
