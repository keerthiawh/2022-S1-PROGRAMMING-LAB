def add_string(strl):
    length=len(strl)
    if length>2:
        if strl[-3:]=='ing':
            strl+='ly'
        else:
            strl+='ing'

    return strl
print(add_string(input("enter a string")))
print(add_string(input("enter a string")))
