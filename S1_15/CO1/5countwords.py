#Count the occurrences of each word in a line of text.
list_words = ["apple","banana","apple","cherry","apple","banana"]
list_words_count = [(x,list_words.count(x)) for x in list_words] 
print("All list ",list_words)
print("Count list ",list_words_count)
