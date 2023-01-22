def convert(str):
    
    l=len(str)
    if(l>2):
        if str[-3:]=='ing':
            print(str+'ly')
        else:
            print(str+'ing')
    else:
        print(str+'ing')
s=input("Enter a string:")
convert(s)
