# (a)Positive numbers
num = [1, -3, 2, 33, -44, 99, 33, -238, 8383]
print(num)
new_lst = [x for x in num if x > 0]
print("Positive numbers =", new_lst)

# (b)Square of N Numbers
sq = [x * x for x in new_lst]
print("Square =",sq)

# (c)Form a list of vowels selected from a given word
vowels = ['a', 'e', 'i', 'o', 'u']
str = input("Enter a string: ")
vowel_list = [x for x in str if x in vowels]
print(vowel_list)

# (d)List Ordinal Values
ord_list = [ord(x) for x in str]
print(ord_list)
