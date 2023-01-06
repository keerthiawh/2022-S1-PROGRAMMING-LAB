def freq():
    test_str=input("enter a string:")
    all_freq={}
    for i in test_str:
        if i in all_freq:
            all_freq[i] +=1
        else:
            all_freq[i] =1
    print("count of all charecters are :\n" +str(all_freq))
freq()
