n=int(input("Enter the number of rows:"))
i=0
while(i<=n):
    j=0
    while(j<i):
        print('*',end='')
        j=j+1
    i=i+1
    print()
i=1
while(i<n):
    j=i;
    while(j<n):
        print('*',end='')
        j=j+1
    i=i+1
    print()
