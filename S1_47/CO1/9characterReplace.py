word = 'onion'
length = len(word)
temp = word[1:length]
temp = temp.replace('o','$')
word = word[0] + temp
print(word)
