def cel(f):
    c=((f-32)*5)/9)
    print("tempurature in celsius:",c)
def far(c):
    f=(c*1.8)+32
    print("tempurature in farenheit:",c)
ch=int(input("enter a choice:  1.celsius to farenheit ,  2.farenheit to celsius"))
if(ch==1):
    print("enter the tempurature in celsius")
