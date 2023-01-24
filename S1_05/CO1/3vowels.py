#Form a list of vowels selected from a given word 
words =  "green"
list_vowels = [i for x in words for i in x if i in "aeiou"]
print("words ", words)
print("Vowel words ", list_vowels)
