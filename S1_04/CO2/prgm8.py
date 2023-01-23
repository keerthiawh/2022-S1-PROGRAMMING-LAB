#Accept a list of words and return length of longest word.
size = int(input("Enter the size of the list : "))
list_words = []
for i in range(size):
    list_words.append(input("Enter the word : "))
print("List is ",list_words)
list_length=[]
for i in list_words:
    list_length.append(len(i))
for i in list_length:
    if i == max(list_length):
        print("The longest word is : ",list_words[list_length.index(i)])
        print("The length of the longest word is : ",max(list_length))
