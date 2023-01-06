def fibernoci(n):
    a,b=1,1
    while a<n:
        print(a)
        a,b=b,a+b
n=int(input("enter the number:"))
fibernoci(n)
