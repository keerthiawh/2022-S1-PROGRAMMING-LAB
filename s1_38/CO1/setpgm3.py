even={2,4,6,8,10,12,14,16,20}
square={1,4,9,16,25,36,49,64,81,100}
uset=even.union(square)
print( "union=",uset)
iset=even.intersection(square)
print("intersection=",iset)
print("difference=",even.difference(square))
