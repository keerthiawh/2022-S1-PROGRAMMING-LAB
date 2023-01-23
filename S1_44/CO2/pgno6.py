def freq():
    test=input("enter a string:")
    dict={}
    for i in test:
        
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    print("Count of all characters are:\n"+str(dict))
freq()
