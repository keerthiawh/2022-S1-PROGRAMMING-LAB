#List ordinal value of each element of a word Hint: use ord() to get ordinal values
word = input("Enter a word: ")
ordinals = [ord(c) for c in word]
print(word)
print("Ordinal valur of ",word," ",ordinals)
