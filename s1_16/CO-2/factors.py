n=int(input("enter number:"))
def factors(X):
    print("The factors of",X,"are:")
    for i in range(1, X + 1):
        if X% i==0:
            print(i)
factors(n)            
