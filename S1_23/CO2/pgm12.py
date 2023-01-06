def addstr(str1):
    l=len(str1)
    if l>2:
        if str1[-3:]=='ing':
            str2=str1+'ly'
        else:
            str2=str1+'ing'
    return str2
s=input("enter a string: ")
string=addstr(s)
print("new string: ",string)
