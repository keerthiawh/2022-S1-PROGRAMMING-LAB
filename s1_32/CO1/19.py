while True:
    
    a=int(input("enter 2 numbers"))
    b=int(input())
    if a==0:
        print(b)
    elif b==0:
        print(a)
    elif a==b:
        print(a)
    elif(a>b):
        print(a-b,b)
    else:print(a,b-a)
    
    choice=int(input("do you want to continue.1:yes 0:no"))
    if choice==0:
        break
               
