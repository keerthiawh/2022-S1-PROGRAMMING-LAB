def count(str1):
    dict={}
    for i in str1:
        keys=dict.keys()
        if i in keys:
            dict[i]=dict[i]+1
        else:
            dict[i]=1
    return dict
name=input("enter a string:")
freq=count(name)
print("the count of characters:",freq)