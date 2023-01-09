n=int(input("Please enter a number:"))
def factors(x):
    print("factors of",x,"are:")
    for i in range(1,x+1):
        if x%i==0:
         print(i)
factors(n)

