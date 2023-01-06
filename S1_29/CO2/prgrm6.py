def sum():
    lst_num=[]
    n=int(input("enter the size:"))
    for i in range(0,n):
        value=int(input())
        lst_num.append(value)
    print(lst_num)
    s=0
    for i in lst_num:
        s=s+i
        i=i+1
    print("the sum is:",s)

sum()
