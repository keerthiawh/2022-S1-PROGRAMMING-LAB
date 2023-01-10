def add_string(str1):
    lenght=len(str1)
    if lenght>2:
        if str1[-3:]=='ing':
            str1+='ly'
        else:
            str1+='ing'

        return str1
print(add_string(input("enter a string:")))
print(add_string(input("enter a string:")))
