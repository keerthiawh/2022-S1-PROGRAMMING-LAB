def longestLength(words):
    finalList = []

    for word in words:
        finalList.append((len(word) , word))

    finalList.sort()

    print("the word with longest length is:", finalList[-1][1]," and length is ",
          len(finalList[-1][1]))
a = input("enter the list")
print(a)
longestLength(a)


    
