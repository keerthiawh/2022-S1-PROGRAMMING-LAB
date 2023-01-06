vowel=['a','e','i','o','u']
name=input("enter a word")
new_word=[x for x in name if x in vowel]
print(new_word)
