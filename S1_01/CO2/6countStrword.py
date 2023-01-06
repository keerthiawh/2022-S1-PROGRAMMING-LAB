#Count the number of characters (character frequency) in a string.
str_words = input("Enter the string : ")
for i in str_words:
    print(i,"=",str_words.count(i))
