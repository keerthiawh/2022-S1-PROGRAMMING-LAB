def count(get_name):
    length=0
    for i in get_name:
        length+=1
    return length
str = input("enter the string:")
length=count(str)
print(length)
