def count(get_name):
    length=0
    for i in get_name:
        length+=i
        return length
str=input("enter the string:")
length=len(str)
print(length)
