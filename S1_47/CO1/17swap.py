#Create a single string separated with space from two strings by swapping the character at position 1 
str_words = input("Enter two words: ")
str_words = str_words.split(" ")
str_words[0],str_words[1] = str_words[1],str_words[0]
print(" ".join(str_words))